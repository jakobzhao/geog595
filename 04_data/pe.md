# Spatial database management using SpatiaLite

**Meeting:** Wednesdays, 2:30 - 5:20, SMI 109

**Instructor:** Bo Zhao, SMI 416B, Office hours by appointment

**Contact:** 206.685.3846, zhaobo@uw.edu, jakobzhao (skype/wechat)


In this practical execerise, we introduce how to manage a spatial database using spatialite. In the GIS industry, there are multiple spatial databases, such as geodatabase, postgresql(with postgis), Oracle, and spatialite. These databases are designed for database of different size and in different uages. Spatialite is a file based database, derived from sqlite and supported by a few open source GIS libraries. Spatailite can be used for mobile development and in cross platform. Since Spatialite can manage both spatial data tables and common attribute data tables in a single database file, it actually makes the geospatial data management much easier if compared with Shapefiles. Besides, SpatiaLite has extended the common SQL functions and supported a series of spatial functions to support advanced spatail queries or joins. Below, the practical exercise will allow the users to learn how to create a spatialite database, to create data table, to insert geospatial data, and eventually visualizes and analyses the geospatial data. This execerise actually extends the [`02_geosearch.py`](../03_bot/02_geosearch.py) from the praticial exercise of last week, the harvested data will save in a spatialite database instead of a csv file.  Okay, let us get started!


## 1. Environment setup

To setup the working environment, you will need to install QGIS 3.+. We assume you have already install Anocanda and PyCharm. QGIS is an integrated GISystem, which has been considered as the open source alternatives to ArcGIS. To install QGIS, make sure its version is greater than 3.0. Please download it from [https://qgis.org/en/site/forusers/download.html](https://qgis.org/en/site/forusers/download.html). In this pratical exercise, we mainly use its `DB Manager` function for spatial data operations.

![](img/dbmanager.png)


## 2. Manage geospatial database using SpatiaLite

### 2.1 Install Prerequisite python libray

Above all, please install one required python libraries - sqlite3. To install, please execute the following script on command prompt (if a windows user) or terminal (if a Mac or Linux user).

```powershell
pip install sqlite3
```

Once installed, please try to execute the script [`tw2db.py`](tw2db.py) under the [04_data folder](./) on PyCharm. We will offer a step-by-step instructon of this piece of python script.

### 2.2 Create a spatialite database

The most convenient way to create a spatialite database is using QGIS. Open a QGIS (version >3.0) application. In the browser panel on the left, please right-click the SpatiaLite icon. In the pop-up dropdown menu, press `Create Database...`. The name of this database is `tweets.db`, which is stored under the [assets](assets/) folder.

![](img/create-database.png)

After inputing the database name and navigate to where to store this database, an empty spatial datbase is generated.

![](img/save-database.png)

### 2.3 Initialize a data table

In order to use this database, we will do several queries to build a data table within the database. The sql statement can be found in [`create_table.sql`](create_table.sql).

Navigate from `Database` on the main menu bar to `DB Manager...`. In the pop-up interface, Right-click the SpatiaLite item on the provider panel to build a new connection. This `New Connection` will conect to `tweets.db`.

![](img/open-spatialite.png)


On the DB Manger interface, Navigate from `Database` on the main menu, and then open up the `SQL window.` In the popup window, please input the first SQL statement, and press `Execute`.

![](img/query-spatialite.png)


Once executed, a new table named `geotweets` is created. This data table has several fields, such as id, username, created_at, lat, lng, and text.


### 2.3 Data Collection

The `on_data` function processes the streamed-in/input data. Let us walk through this function in deatail.

```python
conn = sqlite3.connect(self.dbfile)
cursor = conn.cursor()
```

A spatialite database located at `self.dbfile` will be connected, and a cursor is created for this database as well.


```python
if (time.time() - self.start_time) < self.limit:
        ...
        ...
else:
    conn.close()
    print ("finished.")
    return False
```

This crawler will terminate after reaching the predefined time limit `self.limit`. To stop the database connection, a statement `conn.close()` will be executed.


```python
datajson = json.loads(data)
print (datajson)
id = datajson['id']
username = datajson['user']['screen_name']
created_at = datajson['created_at']
text = datajson['text'].strip().replace("\n", "").replace('"', '\"').replace("'", "\"")

# process the geo-tags
if datajson['coordinates'] == None:
    bbox = datajson['place']['bounding_box']['coordinates'][0]
    lng = (bbox[0][0] + bbox[2][0]) / 2.0
    lat = (bbox[0][1] + bbox[1][1]) / 2.0
else:
    lng = datajson['coordinates']['coordinates'][0]
    lat = datajson['coordinates']['coordinates'][1]
```

The streamed-in data is loaded to a json object `datajson`. A json object is easier to process and destructure. Then, the id, username, and created_at, text as wll as the geographic data are extracted.


```python
insert_record_sql = "INSERT OR REPLACE INTO geotweets (id, username, created_at, lng, lat, text) VALUES (%d, '%s', '%s', %f, %f, '%s')" % (id, username, created_at, lng, lat, text)
cursor.execute(insert_record_sql)
conn.commit()

record = (id, username, created_at, lng, lat, text)
print (record)
```

A sql statement is created, executed and then committed. By this statement, a record will be inserted to this database, if this record has already been inserted, this record will be updated in the data table. To observe the content of the updated record, the record will be outputed to the log.


If `tw2db.py` is executed on PyCharm, a list of records will be inserted to the data table `geotweets` of the databse `tweets.db` under [assets](assets/). To view the inserted data table, execute the following sql statement `select * from geotweets`.

![](img/datatable.png)

### 2.4 Geo-enable the data table


Right now, `geotweets` is still a normal attribute table, it is not geo-enabled. In this subsection, we will add a new geographic column `geom`, and use the `lng` and `lat` column to make a point geographic feature and store it to the `geom` column.

To add a geographic column, run the sql statement below on the query window of QGIS's DB Manager.

```sql
-- Create the geometry column
SELECT AddGeometryColumn('geotweets', 'geom', 4326, 'POINT', 'XY', 0);
```

After executing this sql statement, you can see a new `NULL` column was added to the data table.

![](img/add-geom-column.png)


Then, The geom column will be filled with the point indicating where the geotag for the tweet. The point can be made by the `lat` and `lng` column. Notably, since it is a geographic point, we will also assign a default projection `WGS 84` to this point. The EPSG id of WGS 84 is `4326`. So, the sql statement below will be executed.

```sql
-- Update the geometry column
update geotweets set geom = MakePoint(lng, lat, 4326);
```

Once the sql statement is executed, we need to refresh the DB manager to reload the database change by pressing the first button to the left on the main menu. If switching to the `Preview` tab of the main window, we can actually visualize the `geotweets` data table.

![](img/datatable-preview.png)


### 2.5 And more

#### Build spatial data index and compute boundingbox

To speed up the data search or operation, the spatial data index can be built and the boundingbox can be computed. To do so, please switch to the `info` tab and click on the `find out` and `create it` links.

![](img/index.png)

#### Become a Guru of Spatialite

As a spatial databse, you can conduct spatial query and join. For example, you can generate buffers around each geo-tagged tweet, check which of the geo-tagged tweets fall in the city limits of Seattle. You can compose a (spatial) query on the textbox of the `Query` tab, or you can open the `SQL Query Builder` to help you compose an advanced query. As shown below.

![](img/query-tab.png)


If you want to learn more about SpatiaLite, the materials below are recommended:

- [Basic SQL queries](http://www.gaia-gis.it/gaia-sins/spatialite-cookbook/html/basic-sql.html)
- [Spatial queries](http://www.gaia-gis.it/gaia-sins/spatialite-cookbook/html/first-spatial.html)
- [A quick tutorial to SpatiaLite](http://www.gaia-gis.it/gaia-sins/spatialite-tutorial-2.3.1.html)


#### Visualize geospatial data from a spatialite database

The geospatial data from a spatialite can be visualize and further analyzed in a QGIS environment. To visualize a spatial data table, you need to open `QGIS`, navigate to the `Browser Panel` on the top left, in the `spatialite` categorize, find the spatial date table inside of a spatial database. By clicking on the data table, a new layer will be added to the `Layers Panel` and the layer will be simutanously visualized in the main panel.

![](img/map.png)

Then, you can conduct any spatial anlytical functions onto this spatial layer. If you prefer using ArcGIS platform, you can export the spatial data table as a shapefile for uses in ArcGIS. To do so, right click on the layer `geotweets` in the `Layers Panel`. On the dropdown Menu, choose `Export--> Save Features As...`. On the popup window, choose `ESRI Shapefile` as the export format.

#### Import Data to a Spatialite Database

SpatiaLite can be used to manage spreadsheet and most types of geospatial data. To import data to Spatialite is straightforward. We will walk through the steps as follows. **Note:** You can insert raster data or satelite image as a binary field. We would not introduce in this instruction, but if you are interested in, please read this tutorial on [RasterLite](http://www.gaia-gis.it/gaia-sins/rasterlite-docs/rasterlite-how-to.pdf).

In the [assets](assets/), you will find two data files, in terms of a polygon data [states.geojson](assets/states.geojson) showing the administration boundary of all states in the U.S., and another spreadsheet [pop.csv] containing the population data of each state estimated in 2014 census.

Drag and drop these two files respectively to the `Layers Panel`. Then you will see two layers are listed in the panel and only the states layer is visualized in the map panel. Apparently, the `pop.csv` does not have geometrical feature, so it would not be visualized.

![](img/import.png)

Drag and drop these two layers from the `Layer Panel` to the database file `tweets.db` in the `Browser Panel`. Then, you can immediately see two extra tables are added to the database `tweets.db`.

![](img/drag-to-db.png)

By doing so, the database `tweets.db` can store and manage all the three data tables, in terms of `geotweets`, `states` and `pop`. `geotweets` is points data, `states` is a polygon data, and `pop` is an atrribute data. It is relatively convenient to manage (spatial) databse with spatialite. You do not need to worry about not storing all the assoicted files like shapefile, and it is very easy for data migration and reuse.

## 3. Deliverable

You are excepted to walk through this instruction, try to practice on how to store the geo-tagged tweets to a spatialite database and visualize it in QGIS platform. More importantly, by learning this practical exercise, you are expected to manage the research data on a spatial database.

So, to submit your deliverable, please,
- Share a spatialite database of your research data to the **Canvas Dropbox** of this pratical exercise. (30 POINTS)
- Along with the database, please also attach a word document or a pdf file  to describe what the tables/layers in the database are and how they are related to your research questions. (20 POINTS)


**Note:** Lab assignments are required to be submitted electronically to Canvas unless stated otherwise. Efforts will be made to have them graded and returned within one week after they are submitted.Lab assignments are expected to be completed by the due date. ***A late penalty of at least 10 percentage units will be taken off each day after the due date.*** If you have a genuine reason(known medical condition, a pile-up of due assignments on other courses, ROTC,athletics teams, job interview, religious obligations etc.) for being unable to complete work on time, then some flexibility is possible. However, if in my judgment you could reasonably have let me know beforehand that there would likely be a delay, and then a late penalty will still be imposed if I don't hear from you until after the deadline has passed. For unforeseeable problems,I can be more flexible. If there are ongoing medical, personal, or other issues that are likely to affect your work all semester, then please arrange to see me to discuss the situation. There will be NO make-up exams except for circumstances like those above.
