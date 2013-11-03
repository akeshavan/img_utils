function TifCtrl($scope, $http) {
   // $http.get('ajax?type=index&content=list').success(function(data) {
   //   $scope.pages = data;
   // });

   Dropzone.options.myAwesomeDropzone = {
   init: function() {
         this.on("success", function(file,response){
             var data = $.parseJSON(response)
			 tifDownload(data)

         }); // ends this.on
                    }//ends init function 

 } // ends dropzone options	
	

var tifDownload = function(data){
 	
    $('#downloads').append(downloadstr(data.download,'2'))
    console.log("download "+data.download)
     
 }


function downloadstr (file,span){
	var spanstr = '<div class="spanREPLACE">'
	var href = '<a href="/REPLACE" class="thumbnail">'
	var img = '<img src="/REPLACE" alt="Download Me"></a></div>'
	
	txt = spanstr.replace('REPLACE',span)+href.replace("REPLACE",file)+img.replace("REPLACE",file)
	return txt
}

}// ends function