var mymap = L.map("mapid").setView([12.96, 77.62], 11.5);

L.tileLayer(
  "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw",
  {
    maxZoom: 18,
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
      '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
      'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: "mapbox/streets-v11",
    tileSize: 512,
    zoomOffset: -1
  }
).addTo(mymap);

// L.marker([51.5, -0.09]).addTo(mymap)
//     .bindPopup("<b>Hello world!</b><br />I am a popup.").openPopup();

// Circle heatmap
function callThis(value) {
  console.log(value);
}
function getColour(value) {
  if (value <= 0.1) {
    return "#009933";
  } else if (value <= 0.2) {
    return "#33cc33";
  } else if (value <= 0.3) {
    return "#99ff99";
  } else if (value <= 0.4) {
    return "#ccff99";
  } else if (value <= 0.5) {
    return "#ffff99";
  } else if (value <= 0.6) {
    return "#ffcc00";
  } else if (value <= 0.7) {
    return "#ff5050";
  } else if (value <= 0.8) {
    return "#ff0000";
  } else if (value <= 0.9) {
    return "#ff0000";
  } else {
    return "#b30000";
  }
}

L.circle([12.93, 77.62], 575 * 4, {
  color: "",
  fillColor: getColour(0.191),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("Kormangala Division");

L.circle([12.91, 77.64], 900 * 1.5, {
  color: "",
  fillColor: getColour(0.372),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("HSR Layout");

L.circle([12.97, 77.63], 400 * 6, {
  color: "",
  fillColor: getColour(0.329),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("Indiranagar");

L.circle([12.98, 77.59], 500 * 4, {
  color: "",
  fillColor: getColour(0.426),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("Shivajinagar");

L.circle([13.04, 77.59], 600 * 6, {
  color: "",
  fillColor: getColour(0.392),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("Hebbal");

L.circle([12.96, 77.71], 1000 * 6, {
  color: "",
  fillColor: getColour(0.322),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("Whitefield");

L.circle([13.0, 77.57], 850 * 2, {
  color: "",
  fillColor: getColour(0.5315),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("Malleshwaram");

L.circle([12.98, 77.55], 800 * 3, {
  color: "",
  fillColor: getColour(0.4761),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("Rajaji Nagara Division");

L.circle([12.92, 77.57], 900 * 4.5, {
  color: "",
  fillColor: getColour(0.3272),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("Jayanagar");

L.circle([13.05, 77.5], 700 * 4, {
  color: "",
  fillColor: getColour(0.34),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("Jalahalli");

L.circle([12.92, 77.48], 700 * 5, {
  color: "",
  fillColor: getColour(0.677),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("Kengeri Division");

L.circle([12.94, 77.51], 1000 * 3, {
  color: "",
  fillColor: getColour(0.1676),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("R R NAGAR");

L.circle([12.97, 77.58], 100 * 4, {
  color: "",
  fillColor: getColour(0.289),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("Vidhanasoudha");

L.circle([13.02, 77.52], 1200 * 3, {
  color: "",
  fillColor: getColour(0.286),
  fillOpacity: 0.5
})
  .addTo(mymap)
  .bindPopup("Peenya Division");

// L.polygon([
//     [51.509, -0.08],
//     [51.503, -0.06],
//     [51.51, -0.047]
// ]).addTo(mymap).bindPopup("I am a polygon.");

// var popup = L.popup();

// function onMapClick(e) {
//     popup
//         .setLatLng(e.latlng)
//         .setContent("You clicked the map at " + e.latlng.toString())
//         .openOn(mymap);
// }

// mymap.on("click", onMapClick);
