// var latElement = document.getElementById('lat');
// var latText = latElement.textContent || latElement.innerText;

// var lonElement = document.getElementById('lon');
// var lonText = lonElement.textContent || lonElement.innerText;

//var map = L.map('map').setView([latText, lonText], 10);
var map = L.map('map', {
    minZoom: 0,
    maxZoom: 18,
}).setView([41.8902, 12.4924], 0);

var corner1 = L.latLng(41.90093900, 12.47649200),
    corner2 = L.latLng(41.88153000,12.50767700)
bounds = L.latLngBounds(corner1, corner2);

// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
//     subdomains: ['a','b','c']
// }).addTo(map);


L.tileLayer('static/leaflet/maxarData/{z}/{x}/{y}.png', {
    tms: true,
    // bounds: bounds
}).addTo(map);

// var circleInfo =  {
//     radius: 16000 ,    
//     color: 'red',
//     fillColor: '#f03',
//     fillOpacity: 0.1
// }

// L.circle([latText, lonText], circleInfo).addTo(map)
//     .bindPopup("I am in your crawl space stripping copper wire")
//     .openPopup();

// L.marker([latText, lonText]).addTo(map)
//     .bindPopup("I am in your crawl space stripping copper wire")
//     .openPopup();

// Load and add multiple GeoJSON files (assuming they are in the same directory)
// var shapefiles = [
//         'static/leaflet/22MAR22095810-S2AS-050012575010_01_P001_PIXEL_SHAPE.geojson',
//         'static/leaflet/050012575010_01_ORDER_SHAPE.geojson',
//         'static/leaflet/050012575010_01_PRODUCT_SHAPE.geojson',
//         'static/leaflet/050012575010_01_STRIP_SHAPE.geojson',
//         'static/leaflet/050012575010_01_TILE_SHAPE.geojson'
//     ];

// Load GeoJSON data for each shapefile and add to the map
// for (let i = 0; i < shapefiles.length; i++) {
//     console.log(i)
//     boundary = L.geoJSON.ajax(shapefiles[i]).addTo(map);
//   } 

    // // Define the GeoJSON boundary for the local tiles (replace with your actual boundary)
    // var geojson = {
    //     "type": "Feature",
    //     "geometry": {
    //         "type": "Polygon",
    //         "coordinates": [
    //             [
    //                 [41.90093900, 12.47649200],
    //                 [41.88153000, 12.47649200],
    //                 [41.88153000, 12.50767700],
    //                 [41.90093900, 12.50767700]
    //             ]
    //         ]
    //     }
    // };
    // var boundary = L.geoJSON(geojson).addTo(map);

    //     // Calculate the bounds of your local tiles using the GeoJSON boundary
    //     var localBounds = boundary.getBounds();

    //     // Fit the map view to the bounds of the local tiles **only** (without affecting the base map layer)
    //     map.fitBounds(localBounds, { padding: [10, 10] });

