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
	

Dropzone.options.myAwesomeDropzoneGel = { // The camelized version of the ID of the form element

  // The configuration we've talked about above
  autoProcessQueue: false,
  uploadMultiple: true,
  parallelUploads: 100,
  maxFiles: 100,
  minFiles: 2,

  // The setting up of the dropzone
  init: function() {
    var myDropzone = this;

    // First change the button to actually tell Dropzone to process the queue.
    this.element.querySelector("button[type=submit]").addEventListener("click", function(e) {
      // Make sure that the form isn't actually being sent.
      e.preventDefault();
      e.stopPropagation();
      myDropzone.processQueue();
    });

    // Listen to the sendingmultiple event. In this case, it's the sendingmultiple event instead
    // of the sending event because uploadMultiple is set to true.
    this.on("sendingmultiple", function() {
      // Gets triggered when the form is actually being sent.
      // Hide the success button or the complete form.
    });
    this.on("successmultiple", function(files, response) {
      // Gets triggered when the files have successfully been sent.
      // Redirect user or notify of success.
    });
    this.on("errormultiple", function(files, response) {
      // Gets triggered when there was an error sending the files.
      // Maybe show form again, and notify user of error
    });
  }
 
}


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

