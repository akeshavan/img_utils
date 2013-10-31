/* Controllers */

function IndexCtrl($scope, $http) {
   // $http.get('ajax?type=index&content=list').success(function(data) {
   //   $scope.pages = data;
   // });

   Dropzone.options.myAwesomeDropzone = {
   init: function() {
         this.on("success", function(file){
          
			 mysocket(file);

         }); // ends this.on
                    }//ends init function 

 } // ends dropzone options	
	
var downloads = []	

var downloadhtml= '<div class="span2"><a href="/REPLACE" class="thumbnail"><img src="/REPLACE" alt="Download Me"></a></div>'

	
var mysocket = function (file) {
 	
     s = io.connect('http://' + window.location.hostname + ':8889', {
         rememberTransport: true
     });
    console.log(file.name)
    s.send(file.name)
	// this s.on is happening twice??
    s.on('message', function(data) {
        //console.log($('#downloads').text().indexOf(data))
        var divs = $('#downloads').children()
        var foo = true
        for (var i=0;i<divs.length;i++){
            if ($(divs[i]).children()[0].href.indexOf(data) != -1) { foo=false}
        }
        if (foo){ // if data isn't already in there
            $('#downloads').append(downloadhtml.replace("REPLACE",data).replace('REPLACE',data))
	    console.log("download "+data)
            } //ends index of
 }); // ends s.on
	
 }// ends mysocket




}// ends function

