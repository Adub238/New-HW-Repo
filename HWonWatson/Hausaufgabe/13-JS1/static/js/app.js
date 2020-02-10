// from data.js
var tableData = data;

console.log(data);

// YOUR CODE HERE!
// create table with header columns
var tbody = d3.select('tbody');

//append data.js information to 

function tableTime(data) {
  tbody.html("")  //prevents page from reloading when hit enter
  data.forEach((ufoReport) => {
    var row=tbody.append("tr")
	Object.entries(ufoReport).forEach(([key, value]) => {
		var cell = row.append('td');
		cell.text(value);
		});
  });
}

// create objects for filtering data
var inputField = d3.select('#datetime');
var button = d3.select('#filter-btn');


//use listen to extract information for date search
button.on("click", function() {
   d3.event.preventDefault(); 
  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");
 
//search for information needed
  if (inputValue) {
	var filteredData = tableData.filter(incident => incident.datetime === inputValue);
	tableTime(filteredData);
  }
//export as an array into the console log
  console.log(inputValue);
  console.log(filteredData);

});

tableTime(tableData)


