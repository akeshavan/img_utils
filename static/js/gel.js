function GelCtrl($scope, $http) {


    var gelDownload = function(data){
 	
        $('#geldownloads').append(downloadstr(data.download,'12'))
        console.log("download "+data.download)
        //     } 
     }

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
       var downloadslist = [];
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
	
       this.on("success", function(file,response){
		
           var data = $.parseJSON(response)
   		console.log(downloadslist.indexOf(data.download))
   		if (downloadslist.indexOf(data.download)==-1){
   			gelDownload(data)
   			downloadslist.push(data.download)
   		}
	    

       }); // ends this.on
	
     } // end of init function
   } // ends dropzone options
 
	 function downloadstr (file,span){
	 	var spanstr = '<div class="spanREPLACE">'
	 	var href = '<a href="/REPLACE">Download</a></div>'
	 	var img = '<img src="/REPLACE" alt="Download Me"></a></div>'
	
	 	txt = spanstr.replace('REPLACE',span)+href.replace("REPLACE",file)//+img.replace("REPLACE",file)
	 	return txt
	 }
 
   } // ends function