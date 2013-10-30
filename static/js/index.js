/* Controllers */

function IndexCtrl($scope, $http) {
    $http.get('ajax?type=index&content=list').success(function(data) {
      $scope.pages = data;
    });

    var s = new io.connect('http://' + window.location.hostname + ':8889', {
            rememberTransport: false
        });

    Dropzone.options.myAwesomeDropzone = {
    init: function() {
          this.on("success", function(file){

          console.log(file.name)
          s.send(file.name)
          s.on('message', function(data) {
              $('#chat').append(data); 
       }); // ends s.on

          }); // ends this.on
                     }//ends init function 

  } // ends dropzone options

}// ends function

