# Praticial Exercise 4: Creating geo-narratives with Mapbox storytelling library

**Meeting:** Wednesdays, 2:30 - 5:20, SMI 109

**Instructor:** Bo Zhao, SMI 416B, Office hours by appointment

**Contact:** 206.685.3846, zhaobo@uw.edu, jakobzhao (skype/wechat)

In this pratical exercise, you are expected to make a web based interactive storymap with a storytelling library from Mapbox. Geo-Narrative is an evolving concept in modern cartography and geovisualization, and has been frequently used by Geographers, GIScientists, and Data Journalists. It aims to use differenet geovisual approaches to narrate/represent a geographic phenomenon often in the form of web based interactive maps. From a practical perspective, an attractive and precise geo-narrative should use multiple media instead of only drawing maps. For example, pictures, videos, scripts, audio, and so on can also support the development of a geo-narrative. In recent years, with the convegence of geospatial, information and mobile techiniques, a geo-narrative are integrated with virtual reality, augumented reality, also supported by real-time geospatial data feeds.

**Mapbox storytelling library** is designed to accelerate building out a "scrollytelling" map story. The primary input is a story broken into sections (`chapters`), each hooked to a particular view of a map. You need to input a custom Mapbox Style with layers styled in Studio and toggle the layer's opacity. Below is an example of a geo-narrative made by this library.

![example story screen capture](img/glacierdemo.gif)

You are expected to use `Atom` to make a geo-narrative onto a github repository. A geo-narrative is mainly comprised of html pages and javascript. You can also attach images or videos if needed. For third-party geospatial data, you can use geojson for vectors and WMS (Web Map Services) for rasters. Once the geo-narrative is made, you can synchronize these codes to the cloud side, the GitHub Pages can visualize the codes, and thereby publishing the geo-narratives.

## 1. Preparations

### 1.1 Mapbox registration

To configure and publish a story, you will need a Mapbox [access token](https://docs.mapbox.com/help/glossary/access-token). Please sign up for a free account at [mapbox.com](https://www.mapbox.com/signup/) to get one. You are recommended to use your `edu` email since there are more free resources for students and faculty members.

### 1.2 Map layers design

 Once you are registred, you can also create map layers on [Mapbox Studio](https://studio.mapbox.com). In general, you need to have two types of map layers, base maps (layers) and thematic map layers.

 - **(a)** For base maps, you can visit [mapbox gallery](https://www.mapbox.com/gallery/) for inspiration. I also attach a latest version of [The Guide to Map Design from Mapbox](the-guide-to-map-design.pdf) for your reference.

 ![](img/gallery.png)

- **(b)** If you are planning to include some thematic map layers, you will need some familiarity with [Mapbox Studio](https://studio.mapbox.com). In most cases, you will need to familiar with how to upload and visualize geospatial data on mapbox.

## 2. Development procedure

In this section, you will walk throught the steps of produce a geo-narrative.

### 2.1 Project Initialization



### 2.2 Project Configuration

### 2.3 Storytelling and Prototyping

### 2.4


- Download this repository as a ZIP file using the button above, and unzip it. If you are using `git`, clone this repository.

- If you are new to coding in JavaScript, follow the instructions for Vanilla JS. If you are already working with React, are comfortable with the command line and build systems, and/or want bundled and minified code, choose React.

### Vanilla JS

In your local copy of this repository (the unzipped file you downloaded), navigate to the `src/vanilla-js/` directory.

Make a copy of `config.js.template` and name it `config.js`. Open the new `config.js` file in your text editor.



1. **Select the map style** you want to use (the default is Mapbox Streets, but you can find more here https://docs.mapbox.com/api/maps/#styles, or use one of your custom Studio styles).

2. **Add a Mapbox access token.** A good practice is to [create a separate](https://docs.mapbox.com/help/how-mapbox-works/access-tokens/#creating-and-managing-access-tokens) token per map to be able to track traffic to your different maps.

3. **Choose whether or not to display a marker** at the center of each map location.

4. **Choose a theme for the story text**. There are `light` and `dark` options.

5. **Choose where your story should be aligned over the map**. Options are `center`, `left`, `right`.

```
{
    style: 'mapbox://styles/mapbox/streets-v11',
    accessToken: 'YOUR_ACCESS_TOKEN',
    showMarkers: true,
    alignment: 'left',
    title: 'Story Title Goes Here',
    subtitle: 'A subtitle going into more detail goes here',
    byline: 'By a Digital Storyteller',
    footer: 'Sources and citations, etc. live down at the bottom of the story',
    chapters: [...]
  }
```

6. **Add as many `chapters` in your template as needed.** You'll need a `,` between each section, but no comma at the end. Here is what a `chapter` looks like:

```
        {
            id: 'identifier',
            title: 'Title',
            image: './path/to/image/source.png',
            description: 'Copy these sections to add to your story.',
            location: {
                center: [-77.020636, 38.886900],
                zoom: 13.5,
                pitch: 60,
                bearing: -43.2
            },
            onChapterEnter: [],
            onChapterExit: []
        }
```

7. **Fill out your sections as needed.**  Give each section a unique name in the section `id` property. This will become the HTML `div` `id`, so avoid spaces in the name. The `title`, `description` properties are optional. The `description` supports HTML tags. If you have an image that goes with that section of the story, add the path to the image in the `image` property.

8. For `location`, you can use the `helper.html` file to help you determine the map's position. This tool prints the location settings of the map on the screen in a format ready for copy/paste into the template.

9. Repeat until you have the location entered for each of your sections.

10. Open `index.html` in a browser, and scroll. Voila!

#### Generate Map Position Using `Helper.html`

Using the `helper.html` file, you can search for places, zoom, pan, tilt, and rotate the map to get the desired map position (_Hint_: To tilt and rotate the map, right-click and drag the map).

Notice the location parameters are updated in the upper left corner with everytime you move the map. You can copy the location definition from that page into the `config.js` `location` property section.

There is also a hosted version of this file at [https://demos.mapbox.com/location-helper/](https://demos.mapbox.com/location-helper/)

![location helper screen capture](assets/locationhelper.gif)

#### Configuration File and Layer Settings

Here is a sample configuration:

```
var config = {
    style: 'mapbox://styles/branigan/cjz37rcb003ib1cr3s8rnkt2d',
    accessToken: 'pk.eyJ1IjoibWJ4c29sdXRpb25zIiwiYSI6ImNrMm01aG9hdTBlZGwzbXQ1ZXVrNHNmejAifQ.QHQA0N6XPWddCXtvoODHZg',
    showMarkers: false,
    theme: 'light',
    alignment: 'center',
    title: 'Glaciers of Glacier National Park',
    subtitle: 'Change in coverage from 1998 to 2015',
    byline: '',
    footer: 'Story copy from Wikipedia, map data from USGS',
    chapters: [
        {
            id: 'glacier-np',
            title: 'Glacier National Park Glaciers',
            image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/2015-06-19_Glacier_National_Park_%28U.S.%29_8633.jpg/800px-2015-06-19_Glacier_National_Park_%28U.S.%29_8633.jpg',
            description: 'Glacier National Park is dominated by mountains which were carved into their present shapes by the huge glaciers of the last ice age. These glaciers have largely disappeared over the last 12,000 years. Evidence of widespread glacial action is found throughout the park in the form of U-shaped valleys, cirques, arêtes, and large outflow lakes radiating like fingers from the base of the highest peaks.',
            location: {
                center: [-113.91666, 48.66451],
                zoom: 8,
                pitch: 0.00,
                bearing: 0.00
            },
            onChapterEnter: [
                {
                    layer: 'gnpglaciers-1998',
                    opacity: 0.25
                },
                {
                    layer: 'glaciernp-boundary',
                    opacity: 0.25
                }
            ],
            onChapterExit: [
              {
                  layer: 'gnpglaciers-1998',
                  opacity: 0.25
              },
              {
                  layer: 'glaciernp-boundary',
                  opacity: 0
              }
            ]
        },
        {
            id: 'harrison1998',
            title: 'Harrison Glacier, 1998',
            image: '',
            description: 'Harrison Glacier is located in the US state of Montana in Glacier National Park. Situated on a southeast facing ridge immediately south of Mount Jackson, Harrison Glacier is the largest glacier in Glacier National Park.',
            location: {
                center: [-113.72917, 48.58938],
                zoom: 12.92,
                pitch: 39.50,
                bearing: 36.00
            },
            onChapterEnter: [],
            onChapterExit: []
        }
    ]
}
```

#### Configuration Options

Note: items in bold are **required**.

**`style`**: This is the Mapbox style `url` to use for the app. It can be a standard style, or a custom style from your Mapbox account. Use a custom style if you want to include custom data or layers.

**`accessToken`**: Your Mapbox access token.

**`showMarkers`**: This controls whether markers are shown at the centerpoint of each chapter. If `true`, the map will display a default blue, inverted-teardrop icon.

**`theme`**: Two basic themes (light and dark) are available.

**`alignment`**: This defines where the story text should appear over the map. Options are `center`, `left`, and `right`. When the browser window is less than 750 pixels wide, the story will be `center` aligned.

`title`: The title of the overall story. (Optional)

`subtitle`: A subtitle for the story. (Optional)

`byline`: Credit the author of the story. (Optional)

`footer`: Citations, credits, etc. that will be displayed at the bottom of the story.

**`chapters`**: This contains all of the story content and map controls for each section of the story. _Array of objects_

- **`id`**: A slug-style ID for the chapter. This is read by the JavaScript driving the app and is assigned as an HTML `id` for the `div` element containing the rest of the story. A best-practice format would be to use kebab case, like `my-story-chapter-1`.
- `title`: The title of the section, displayed in an `h3` element.
- `image`: The path to an image to display in this section.
- `description`: The main story content for the section. This should be aligned with what the reader is seeing on the map. In the vanilla version, this field will render as HTML. Images, links, and other items can be included as HTML.
- **`location`**: Details about the map display and camera view.
    - **`center`**: Center coordinates of the map, as `longitude, latitude`
    - **`zoom`**: Zoom level of the map.
    - **`pitch`**: Angle of the map view. `0` is straight down, and `60` is highly tilted.
    - **`bearing`**: Degrees of rotation clockwise from North (`0`). Negative values represent counter-clockwise rotation.
- `onChapterEnter`: Layers to be displayed/hidden/muted when the section becomes active. _Array of objects_
    - `layer`: Layer name as assigned in Mapbox Studio.
    - `opacity`: The opacity to display the layer. `0` is fully transparent, `1` is fully opaque.
- `onChapterExit`: Same as `onChapterEnter` except it is triggered when the section becomes inactive. _Array of objects_


#### Mapbox Studio Style Configuration

Add and style each custom layer in your Studio style. Before the final publish, set any layers's style to be hidden with `0` opacity. **Do not hide the layer**. For example, if you have a `circle` layer, makes sure the `color-opacity` and/or the `stroke-opacity` is set to 0.

This will ensure that the map appears correctly when the story page loads. To adjust the opacity of the layers as the reader scrolls through the story, use the `onChapterEnter` or `onChapterExit` configuration options to set your desired opacity for the layer.


## Acknowledgments

* John Branigan on the Mapbox [Solutions Architecture Team](mailto:solutions_architecture@mapbox.com)
* Lo Bénichou for the idea, support, and awesome feedback throughout the design and build process
* Paige Moody and Lem Thornton for early testing and feedback
* Chris Toomey for ushering this work through and keeping things on track
* Journalists with stories that help us make sense of what goes around us

**The instruction of this exercise has learnt and even directly copied a few open-source Mapbox archives and documentations, but I made necessary edits to better facilite the course requirements and demands. If you believe it has viloated any Mapbox rules, please contact me via zhaobo@uw.edu.**
