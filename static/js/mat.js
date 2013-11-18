function MatCtrl($scope, $http) {
   // $http.get('ajax?type=index&content=list').success(function(data) {
   //   $scope.pages = data;
   // });

   Dropzone.options.matDropzone = {
	   
       //autoProcessQueue: false,
       uploadMultiple: true,
       parallelUploads: 100,
       maxFiles: 100,
       //minFiles: 2,
	   
   init: function() {
         var downloadslist = [];
		 this.on("success", function(file,response){
             var data = $.parseJSON(response)
	    		if (downloadslist.indexOf(data.download)==-1){
	    			matDownload(data)
	    			downloadslist.push(data.download)
					console.log(data)
					
					if (data.hasOwnProperty("vals")){
						dod3plot(data.vals)
					}
	    		}
	    
         }); // ends this.on
                    }//ends init function 

 } // ends dropzone options	
	

var matDownload = function(data){
 	
    $('#matdownloads').append(downloadstr(data.download,'12'))
    console.log("download "+data.download)
     
 }


function downloadstr (file,span){
	var spanstr = '<div class="spanREPLACE">'
	var href = '<a href="/REPLACE" class="thumbnail">'
	var img = '<img src="/REPLACE" alt="Download Me"></a></div>'
	
	txt = spanstr.replace('REPLACE',span)+href.replace("REPLACE",file)+img.replace("REPLACE",file)
	return txt
}


function dod3plotbad(vals){
	
	console.log(vals.roi)
	console.log(vals.mean)
	var chart = d3.select("#d3plot").append("svg")
	    .attr("class", "chart")
	    .attr("width", 420)
	    .attr("height", 20 * vals.roi.length);
	
    var x = d3.scale.linear()
        .domain([0, d3.max(vals.roi)])
        .range([0, 420]);
	
	chart.selectAll("rect")
	     .data(vals.mean)
	     .enter().append("rect")
	     .attr("y", function(d, i) { return i * 20; })
	     .attr("width", x)
	     .attr("height", 20);
	
}



function dod3plot(vals){
	
	var margin = {top: 40, right: 20, bottom: 30, left: 40},
	    width = 600 - margin.left - margin.right,
	    height = 1000 - margin.top - margin.bottom;

	var formatPercent = d3.format(".0%");

	var x = d3.scale.ordinal()
	    .rangeRoundBands([0, width], .1);

	var y = d3.scale.linear()
	    .range([height, 0]);

	var xAxis = d3.svg.axis()
	    .scale(x)
	    .orient("bottom");

	var yAxis = d3.svg.axis()
	    .scale(y)
	    .orient("left")
	    //.tickFormat(formatPercent);

	var tip = d3.tip()
	  .attr('class', 'd3-tip')
	  .offset([0, 0])
	  .html(function(d) {
	    return "<strong>Mean:</strong> <span style='color:red'>" + d.mean + "</span>";
	  })

	var svg = d3.select("#d3plot").append("svg")
	    .attr("width", width + margin.left + margin.right)
	    .attr("height", height + margin.top + margin.bottom)
	  .append("g")
	    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	svg.call(tip);

	d3.tsv(vals, type, function(error, data) {
	  x.domain(data.map(function(d) { return d.roi; }));
	  y.domain([0, d3.max(data, function(d) { return d.mean; })]);
      console.log(y)
	  svg.append("g")
	      .attr("class", "x axis")
	      .attr("transform", "translate(0," + height + ")")
	      .call(xAxis);

	  svg.append("g")
	      .attr("class", "y axis")
	      .call(yAxis)
	    .append("text")
	      .attr("transform", "rotate(-90)")
	      .attr("y", 6)
	      .attr("dy", ".71em")
	      .style("text-anchor", "end")
	      .text("Mean");

	  svg.selectAll(".bar")
	      .data(data)
	    .enter().append("rect")
	      .attr("class", "bar")
	      .attr("x", function(d) { return x(d.roi); })
	      .attr("width", x.rangeBand())
	      .attr("y", function(d) { return y(d.mean); })
	      .attr("height", function(d) { return height - y(d.mean); })
	      .on('mouseover', tip.show)
	      .on('mouseout', tip.hide)

	});

	function type(d) {
	  d.roi = d.roi;
	  return d;
	}

}
	

}// ends function