// @TODO: YOUR CODE HERE!
//set up the graph 
var svgheight = 890;
var svgwidth = 790;
//var padding = 20

var margin = {
    top: 20,
    right: 10,
    bottom: 60,
    left:  40
};

var width = svgwidth - margin.left - margin.right;
var height = svgheight - margin.top - margin.bottom;

//create a function to develop elements to generate the graph 

var svg = d3.select("#scatter")
               .append("svg")
               .attr("width", svgwidth)
               .attr("height", svgheight)
               .attr("class", "chart");

var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);


//import data

d3.csv("assets/data/datahealth.csv").then(function(dataHealth) {
     dataHealth.forEach(function(data) {
         data.heathcare = +data.healthcare;
         data.income = +data.income;
         data.abbr = data.abbr;
//       console.log("healthcare", data.healthcare);
//        console.log("income", data.income);
     });
     
     
     //create the scales --> input, domain, output, range

     var xscale1 = d3.scaleLinear()
        .domain([((d3.min(dataHealth, d => d.income) - 2000)/ 1000), 
                     ((d3.max(dataHealth, d => d.income) + 2000) / 1000)])
        .range([0, width]);
     
     var yscale1 = d3.scaleLinear()
        .domain([4,26])
       .range([height, 0]);
    
     //add axes
     var xAxis1 = d3.axisBottom(xscale1);

     var yAxis1 = d3.axisLeft(yscale1).ticks(8);
    

    

     //import the elements into svg

     chartGroup.append("g")
					.attr("transform", `translate(0, ${height})`)
					.call(xAxis1);

    chartGroup.append("g")
				   .call(yAxis1);

    var circlesGroup = chartGroup.selectAll("circle")
											.data(dataHealth)
											.enter()
											.append("circle")
											.attr("cx", d => xscale1(d.income / 1000))
											.attr("cy", d => yscale1(d.healthcare))
											.attr("r", "10")
											.attr("fill", "navy");
  
    var stateGroup = chartGroup.selectAll("svg")
										   .data(dataHealth)
										   .enter()
										   .append("text")
										   .text(function(d) {return d.abbr;})
										   .attr("dx",d => xscale1(d.income / 1000))
										   .attr("dy", d => yscale1(d.healthcare)+ 4)
										   .attr("font-size", "8")
										   .attr("stroke", "white")
										   .attr("class", "stateText");

     //create axis labels
     chartGroup.append("text")
					.attr("transform", `translate(${width / 2 - 40}, ${height + margin.top + 30})`)
					.attr("class", "axisText")
					.text("Average Income (in Thousands)");

    chartGroup.append("text")
				   .attr("transform", "rotate(-90)")
				   .attr("y", 0 - margin.left)
				   .attr("x", 0 - (height / 2))
				   .attr("dy", "1em")
				   .attr("class", "axisText")
				   .text("% Without Healthcare");
    datahealth();
    }).catch(function(error) {
});






   
