var layerTypes = {
  'fill': ['fill-opacity'],
  'line': ['line-opacity'],
  'circle': ['circle-opacity', 'circle-stroke-opacity'],
  'symbol': ['icon-opacity', 'text-opacity'],
  'raster': ['raster-opacity'],
  'fill-extrusion': ['fill-extrusion-opacity']
}

var alignments = {
  'left': 'lefty',
  'center': 'centered',
  'right': 'righty',
  'full': 'fully'
}

function getLayerPaintType(layer) {
  var layerType = map.getLayer(layer).type;
  return layerTypes[layerType];
}

function setLayerOpacity(layer) {
  var paintProps = getLayerPaintType(layer.layer);
  paintProps.forEach(function(prop) {
    map.setPaintProperty(layer.layer, prop, layer.opacity);
  });
}

var story = $('#story')[0];


var features = document.createElement('div');
$(features).addClass(alignments[config.alignment]);
// features.classList.add();
features.setAttribute('id', 'features');

var header = document.createElement('div');

if (config.title) {
  var titleText = document.createElement('h1');
  titleText.innerText = config.title;
  $(header).append(titleText);
  // header.appendChild(titleText);
}

if (config.subtitle) {
  var subtitleText = document.createElement('h2');
  subtitleText.innerText = config.subtitle;
  // header.appendChild(subtitleText);
  $(header).append(subtitleText);
}

if (config.byline) {
  var bylineText = document.createElement('p');
  bylineText.innerText = config.byline;
  // header.appendChild(bylineText);
  $(header).append(bylineText);
}

if (header.innerText.length > 0) {
  $(header).addClass(config.theme);
  // header.classList.add(config.theme);
  $(header).attr('id', 'header');
  // header.setAttribute('id', 'header');
  // story.appendChild(header);
  $(story).append(header);
}

config.chapters.forEach((record, idx) => {
  var container = document.createElement('div');
  var chapter = document.createElement('div');

  if (record.title) {
    var title = document.createElement('h3');
    title.innerText = record.title;
    $(chapter).append(title);
  }

  if (record.image) {
    var image = new Image();
    image.src = record.image;
    $(chapter).append(image);
  }

  if (record.description) {
    var desc = document.createElement('p');
    desc.innerHTML = record.description;
    $(chapter).append(desc);
  }

  $(container).attr('id', record.id);
  // container.setAttribute('id', record.id);
  $(container).addClass('step');
  // container.classList.add('step');
  if (idx === 0) {
    $(container).addClass('active');
    // container.classList.add('active');
  }

  $(chapter).addClass(config.theme);
  $(chapter).addClass(record.type);
  $(container).append(chapter);
  // container.appendChild(chapter);
  $(features).append(container);
  // features.appendChild(container);
});

$(story).append(features);

var footer = document.createElement('div');

if (config.footer) {
  var footerText = document.createElement('p');
  footerText.innerHTML = config.footer;
  $(footer).append(footerText);
}

if (footer.innerText.length > 0) {
  footer.classList.add(config.theme);
  footer.setAttribute('id', 'footer');
  $(story).append(footer);
}

mapboxgl.accessToken = config.accessToken;

const transformRequest = (url) => {
  const hasQuery = url.indexOf("?") !== -1;
  const suffix = hasQuery ? "&pluginName=journalismScrollytelling" : "?pluginName=journalismScrollytelling";
  return {
    url: url + suffix
  }
}

var map = new mapboxgl.Map({
  container: 'map',
  style: config.style,
  center: config.chapters[0].location.center,
  zoom: config.chapters[0].location.zoom,
  bearing: config.chapters[0].location.bearing,
  pitch: config.chapters[0].location.pitch,
  scrollZoom: false,
  transformRequest: transformRequest
});

var marker = new mapboxgl.Marker();
if (config.showMarkers) {
  marker.setLngLat(config.chapters[0].location.center).addTo(map);
}

// instantiate the scrollama
var scroller = scrollama();

map.on("load", function() {
  // setup the instance, pass callback functions
  scroller
    .setup({
      step: '.step',
      offset: 0.3,
      progress: true
    })
    .onStepEnter(response => {
      var chapter = config.chapters.find(chap => chap.id === response.element.id);
      $(response.element).addClass('active');
      // response.element.classList.add('active');
      map.flyTo(chapter.location);
      if (config.showMarkers) {
        marker.setLngLat(chapter.location.center);
      }
      if (chapter.onChapterEnter.length > 0) {
        chapter.onChapterEnter.forEach(setLayerOpacity);
      }

      if (chapter.type === 'image') {
        $('.image').addClass("fullscreen-background-image")
        $('.fullscreen-background-image').css(
          {
          'background': 'url("img/uw.jpg") no-repeat center center fixed',
          '-webkit-background-size': 'cover',
          '-moz-background-size': 'cover',
          '-o-background-size': 'cover',
          'background-size': 'cover',
          'position': 'absolute',
          'min-height': '100vh',
          'min-width': '100vw',
          'z-index': '10000',
          'top': '0',
          'right': '0',
          'bottom': '0',
          'left': '0',
          'display': 'block'
        });
      }


    })
    .onStepExit(response => {
      var chapter = config.chapters.find(chap => chap.id === response.element.id);
      $(response.element).removeClass('active');
      // response.element.classList.remove('active');
      if (chapter.onChapterExit.length > 0) {
        chapter.onChapterExit.forEach(setLayerOpacity);
      }

      // if (chapter.type === 'image') {
        $('.image').removeClass("fullscreen-background-image")
      // }
    });
});

// setup resize event
window.addEventListener('resize', scroller.resize);
