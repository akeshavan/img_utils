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
	
$scope.downloads = ["one download"]	
	
 var mysocket = function (file) {
 	
     s = io.connect('http://' + window.location.hostname + ':8889', {
         rememberTransport: true
     });
    console.log(file.name)
    s.send(file.name)
	// this s.on is happening twice??
    s.on('message', function(data) {
        $('#downloads').append('<button class="btn btn-success">Download</button>')
	 console.log("download "+data)
 }); // ends s.on
	
 }// ends mysocket




}// ends function

