<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="http://labratrevenge.com/d3-tip/javascripts/d3.tip.min.js"></script>

<div class="tab-pane" id="mat"  ng-controller="MatCtrl" ng-model-instant>
  
    <div class="jumbotron">
    <h1>Mat Viewer</h1>
    Drag and Drop your .mat files to view as images</p>

    </div>

    <form action="/mat-upload"
    class="dropzone dz-clickable"
    enctype="multipart/form-data"
    id="mat-dropzone"></form>

    <div id="matdownloads">
       
		

		<div class="span12" id="d3plot">
		</div>
	</div>


</div>