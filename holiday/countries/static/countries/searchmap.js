var map = L.map('map').setView([0, 0], 2);
L.tileLayer('https://{s}.tile.osm.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
L.Control.geocoder().addTo(map);
