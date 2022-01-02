--created on Dec 24, 2020
--@author:          Bo Zhao
--@email:           zhaobo@uw.edu
--@website:         https://hgis.uw.edu
--@organization:    Department of Geography, University of Washington, Seattle
--@description:     create a spatialite database on QGIS's database manager

-- Create the data table
CREATE TABLE IF NOT EXISTS geotweets (
    id INTEGER PRIMARY KEY,
    username  TEXT NOT NULL,
    created_at TEXT DEFAULT 0,
    lat REAL DEFAULT 0,
    lng REAL DEFAULT 0,
    text TEXT
);

-- Create the geometry column
SELECT AddGeometryColumn('geotweets', 'geom', 4326, 'POINT', 'XY', 0);

-- Update the geometry column
update geotweets set geom = MakePoint(lng, lat, 4326);
