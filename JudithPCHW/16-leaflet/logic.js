var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: "pk.eyJ1IjoiYWR1YjIzOCIsImEiOiJjazY1YjlmOG4wazh1M2xvZDZ0bnppcmhlIn0.M2cqyZ6e_8otafptnhBMHQ"
});

var myMap = L.map("map", {
    center: [40.42, -3.70],
    zoom: 2.3,
     maxZoom: 25
});

lightmap.addTo(myMap);

//get the data and create the markers and legends

d3.json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson", 
function(data) { 
    //create function to place the markers
    function setMarks(feature) {
        return {
            fillColor: chooseColor(feature.properties.mag),
            color: chooseColor(feature.properties.mag),
            radius: chooseRadius(feature.properties.mag),
            fillOpacity: 4
        };
    }
    //function for the radius
    function chooseRadius(magnitude) {
        return magnitude * 2.5;
    }
    //function for the color
    function chooseColor(magnitude) {
        switch(true) {
            case magnitude > 6:
                return "#FF0000";
            case magnitude > 5:
                return "#FF4000";
            case magnitude > 4:
                 return "#FF8000";
            case magnitude > 3:
                return "#FFBF00";
            default:
                return "#FFFF00";
        };
    }
    //add the circle markers and the popups to the map
    L.geoJson(data, {
        pointToLayer: function(feature, latlng) {
                return L.circleMarker(latlng);
        },
        style: setMarks,

        onEachFeature: function(feature, layer) {
            layer.bindPopup("Earthquake Magnitude: " + feature.properties.mag + "<br>Location of Earthquake: " + feature.properties.place);
        }
    }).addTo(myMap)
});
//create a legend
var legend = L.control({position: "bottomright" });


legend.onAdd = function() {
        var div = L.DomUtil.create("div", "info legend");
        var grades = [2, 3, 4, 5, 6];
        var colors = ["#FFFF00", "#FFBF00", "#FF8000", "#FF4000", "#FF0000"];
        var labels = ['<strong>Magnitudes</strong>'];

                 
        
        for (var i = 0; i < grades.length; i++) {
           var fromMag = grades[i];
           var toMag = grades[i+1];
           labels.push('<i style="background:' + colors[i] + '"></i>&nbsp&nbsp&nbsp' + 
                fromMag + (toMag ? '&ndash;' + toMag : '+'));
            }
        div.innerHTML = labels.join('<br>');
        return div;
};

legend.addTo(myMap);
