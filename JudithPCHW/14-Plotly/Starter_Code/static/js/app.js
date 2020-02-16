///import the json file

var file = 'samples.json' ;
d3.json(file).then(function(data){
    console.log(data);
 });


//create the array and append to the html

function watchBacteriaGrow(sample) {
    d3.json(file).then(function(data){
        var metadata = data.metadata;
        var array = metadata.filter(person => person.id == sample);
        var result = array[0];
        console.log(result);
        var patient = d3.select("#sample-metadata");
        var id = result.id;
        console.log(id);
        sortSample(id);
        patient.html("");
        Object.entries(result).forEach(([key, value]) => {
            patient.append("p").text(`${key}: ${value}`);
        });
    });
}

//Fill in the dropdown and select the initial value for the dropdown
function startPage() {
    d3.json(file).then(function(data) {
            var dropDown = d3.select("#selDataset");
            var id = data.name;
            var samples = [];
            var samples = data.names;
  //          console.log(samples);
            var initialSample = samples[0];
            
            
            function builddropDown() {
             for (var i=0; i< samples.length; i++) {
                 dropDown.append("option").text(samples[i]).property("value", samples[i]);
                }
            };
            watchBacteriaGrow(initialSample);
            builddropDown();
           
         });
}
startPage();

//change the selector to choose a different patient (starter code has in HTML an optionChanged in it)

function optionChanged(data) {
    watchBacteriaGrow(data);
}

//Must slice the top 10 values for the value being sent and build the charts

function sortSample(id) {
    d3.json(file).then(function(data) {
        console.log("id:", id);
        var samples = data.samples;
        var selectedSample = samples.filter(samples => samples.id == id);
        var result = selectedSample[0];
		var otu_ids = result.otu_ids;
		var otu_labels = result.otu_labels;
		var sample_values = result.sample_values;
        console.log("table to sort", result);
		var slicedIds = result.otu_ids.slice(0, 10);
		console.log(slicedIds);
		reversedIds = slicedIds.reverse();
		console.log(reversedIds);
		var slicedLabels = result.otu_labels.slice(0, 10);
		console.log(slicedLabels);
		reversedLabels = slicedLabels.reverse();
		console.log(reversedLabels);
		var slicedSamples = result.sample_values.slice(0, 10);
		console.log(slicedSamples);
		reversedSamples = slicedSamples.reverse();
		console.log(slicedSamples);

    var yBar = reversedIds.map(reversedIds => `OTU ${reversedIds}`);
     var barGraph = [{ 
         x: reversedSamples,
         y: yBar,
         type: "bar",
         orientation: "h",
         text: reversedLabels,
     }];
     var barLayout = {
         title: "Most Common Bacteria for Selected Patient",
     };
     Plotly.newPlot("bar",barGraph, barLayout);

     var bubbleChart = [{
        x: otu_ids,
		y: sample_values,
        text: otu_labels,
		mode: "markers",
        marker: {
              color: otu_ids,
              size: sample_values}
        }];
    
    var bubbleLayout = {
           title: "Frequency of Bacteria per Sample",
           showlegend: false,
           xaxis: { title: "Bacteria ID"},
    };
    Plotly.newPlot("bubble", bubbleChart, bubbleLayout);


    });


}
