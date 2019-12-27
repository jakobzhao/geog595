var config = {
  style: "mapbox://styles/branigan/ck21y6cbi05cv1cn3gvbvykyd",
  accessToken:
    "pk.eyJ1IjoibWJ4c29sdXRpb25zIiwiYSI6ImNrMm01aG9hdTBlZGwzbXQ1ZXVrNHNmejAifQ.QHQA0N6XPWddCXtvoODHZg",
  showMarkers: false,
  theme: "dark",
  alignment: "left",
  title: "Scrollytelling with Mapbox Example",
  subtitle: "A low-code template to help you tell your map-based story",
  byline: "By Mapbox Solutions Architecture",
  footer: "Sources: U.S. Census Bureau, American Community Survey, Max Planck Institute for Ornithology, USDA National Agricultural Statistics Service",
  chapters: [
    {
      id: "county-circles-1",
      title: "What does this template do?",
      image: "https://cdn.glitch.com/b42de0da-ef6b-4756-9c86-4c46809f1380%2Fmapbox-logo-white.png?v=1571949196003",
      description:
        "An approach to interactive storytelling, where the graphics unfold as the user scrolls through the story, is known as “scrollytelling”. The scrollytelling template was designed and built to accelerate the process of creating a map-based story. ",
      location: {
        center: [-97.061, 38.39659],
        zoom: 3.3,
        pitch: 0.0,
        bearing: 0.0
      },
      onChapterEnter: [
        {
          layer: "county-pop-centroid",
          opacity: 0.5
        }
      ],
      onChapterExit: [
        {
          layer: "county-pop-centroid",
          opacity: 0
        }
      ]
    },
    {
      id: "county-circles-2",
      title: "Control the map",
      image: "",
      description:
        "Zoom, pan, tilt, and rotate the map to higlight the geographic area related to this part of your story.",
      location: {
        center: [-80.70604, 36.22582],
        zoom: 5.7,
        pitch: 60.0,
        bearing: 0.0
      },
      onChapterEnter: [
        {
          layer: "county-pop-centroid",
          opacity: 0.5
        }
      ],
      onChapterExit: [
        {
          layer: "county-pop-centroid",
          opacity: 0
        }
      ]
    },
    {
      id: "county-polys-1",
      title: "Change the layers",
      image: "",
      description:
        "If you have set up custom map data in Mapbox Studio, there are also settings to control which map layers to show and hide.",
      location: {
        center: [-80.70604, 36.22582],
        zoom: 5.7,
        pitch: 60.0,
        bearing: 0.0
      },
      onChapterEnter: [
        {
          layer: "county-pop-polygon",
          opacity: 0.5
        }
      ],
      onChapterExit: [
        {
          layer: "county-pop-polygon",
          opacity: 0
        }
      ]
    },
    // {
    //     id: 'county-polys-2',
    //     title: 'Display Title',
    //     image: '',
    //     description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    //     location: {
    //       center: [-76.20138, 41.65058],
    //       zoom: 6.61,
    //       pitch: 59.50,
    //       bearing: -35.20
    //     },
    //     onChapterEnter: [
    //         {
    //             layer: 'county-pop-polygon',
    //             opacity: 0.5
    //         }
    //     ],
    //     onChapterExit: [
    //         {
    //             layer: 'county-pop-polygon',
    //             opacity: 0
    //         }
    //     ]
    // },
    {
      id: "freedom-1",
      title: "Layer support",
      image: "",
      description:
        "This template supports circle, line, fill, symbol, fill-extrusion, and raster layers.",
      location: {
        center: [-81.38123, 35.85894],
        zoom: 7.51,
        pitch: 60.0,
        bearing: 38.4
      },
      onChapterEnter: [
        {
          layer: "freedom-line",
          opacity: 0.3
        }
      ],
      onChapterExit: [
        {
          layer: "freedom-line",
          opacity: 0
        }
      ]
    },
    // {
    //     id: 'freedom-2',
    //     title: 'Display Title',
    //     image: '',
    //     description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    //     location: {
    //       center: [-82.69756, 34.59881],
    //       zoom: 9.39,
    //       pitch: 60.00,
    //       bearing: 38.40
    //     },
    //     onChapterEnter: [
    //         {
    //             layer: 'freedom-line',
    //             opacity: 0.3
    //         }
    //     ],
    //     onChapterExit: [
    //         {
    //             layer: 'freedom-line',
    //             opacity: 0
    //         }
    //     ]
    // },
    {
      id: "raster-1",
      title: "Your data and Mapbox data",
      image: "",
      description:
        "You can control any data in your Studio style, including base map layers. Shown in green are national park areas.",
      location: {
        center: [-107.061, 38.39659],
        zoom: 7,
        pitch: 60.0,
        bearing: 0
      },
      onChapterEnter: [
        {
          layer: "national-park",
          opacity: 0.5
        }
      ],
      onChapterExit: [
        {
          layer: "national-park",
          opacity: 0
        }
      ]
    },
    {
      id: "raster-2",
      title: "Guide your reader's eye",
      image: "",
      description:
        "We also built a page to help find location coordinates and set up the best \"camera angle\" to showcase a location. Find the helper at <a href='https://demos.mapbox.com/location-helper/'>https://demos.mapbox.com/location-helper/</a>.",
      location: {
        center: [-119.55048, 36.03344],
        zoom: 11.1,
        pitch: 55.5,
        bearing: -115.2
      },
      onChapterEnter: [
        {
          layer: "cdl-2018",
          opacity: 0.5
        }
      ],
      onChapterExit: [
        {
          layer: "cdl-2018",
          opacity: 0
        }
      ]
    },
    {
      id: "wrap-up",
      title: "",
      image: "",
      description:
        "The hard part still may be coming up with a story, but now it's a little easier to tell. Built with Mapbox GL JS, Scrollama.js, and JavaScript. Learn more at <a href='https://www.mapbox.com/solutions/interactive-storytelling/'>https://www.mapbox.com/solutions/interactive-storytelling/</a>",
      location: {
        center: [-97.061, 38.39659],
        zoom: 3.3,
        pitch: 0.0,
        bearing: 0.0
      },
      onChapterEnter: [
        {
          layer: "county-pop-centroid",
          opacity: 0.5
        }
      ],
      onChapterExit: [
        {
          layer: "county-pop-centroid",
          opacity: 0
        }
      ]
    }
  ]
};
