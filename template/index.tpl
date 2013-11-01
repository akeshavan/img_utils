{% extends "base.tpl" %}

{% block head %}
    
<style type="text/css">
      body {
        padding-top: 20px;
        padding-bottom: 60px;
      }

      /* Custom container */
      .container {
        margin: 0 auto;
        max-width: 1000px;
      }
      .container > hr {
        margin: 60px 0;
      }

      /* Main marketing message and sign up button */
      .jumbotron {
        margin: 80px 0;
        text-align: center;
      }
      .jumbotron h1 {
        font-size: 100px;
        line-height: 1;
      }
      .jumbotron .lead {
        font-size: 24px;
        line-height: 1.25;
      }
      .jumbotron .btn {
        font-size: 21px;
        padding: 14px 24px;
      }

      /* Supporting marketing content */
      .marketing {
        margin: 60px 0;
      }
      .marketing p + h4 {
        margin-top: 28px;
      }
      .tabs-left {
        margin: 60px 0;
      }
    </style>

{% end %}

{% block body %}


<div class="container" ng-controller="IndexCtrl">

	<div class="navbar navbar-inverse navbar-fixed-top">
	      <div class="navbar-inner">
	        <div class="container">
	          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
	            <span class="icon-bar"></span>
	            <span class="icon-bar"></span>
	            <span class="icon-bar"></span>
	          </button>
	          <a class="brand" href="#">{{ project_name }}</a>
	          <div class="nav-collapse collapse">
	            <ul class="nav">
	              <li class="active"><a href="#">Home</a></li>
	              <li><a href="#about">About</a></li>
	              <li><a href="#contact">Contact</a></li>
	            </ul>
	          </div><!--/.nav-collapse -->
	        </div>
	      </div>
	    </div>
		
	<div class="row-fluid">
		<div class="tabbable tabs-left"> <!-- Only required for left/right tabs -->
		  <ul class="nav nav-tabs">
		    <li class="active"><a href="#tif" data-toggle="tab">Section 1</a></li>
		    <li><a href="#gel" data-toggle="tab">Section 2</a></li>
		  </ul>
		  
		  <div class="tab-content">
		    <div class="tab-pane active" id="tif"  ng-model-instant>
		      
			    <div class="jumbotron">
			    <h1>TIF converter</h1>
			    Drag and Drop your .tif files to convert them to high quality JPEGs
			    <p>For the Douglas Lab at UCSF, to convert Typhoon .tif images</p>

			    </div>
  
		        <form action="/file-upload"
		        class="dropzone dz-clickable"
		        enctype="multipart/form-data"
		        id="my-awesome-dropzone"></form>
  
			    <div id="downloads">
                   
					
	   
				</div>
  
  
		    </div>
			
		    <div class="tab-pane" id="gel">
			    <div class="jumbotron">
			    <h1>Gel Analysis</h1>
			    Automated Gel Analysis pipeline
			    <p>Brought to you by the Douglas Lab</p>

			    </div>
                        <h2> Please Upload a Cy3 and Cy5 image</h2>
		      
		        <form class="dropzone" action="/file-upload-gel"
		        enctype="multipart/form-data"
		        id="my-awesome-dropzone-gel">
                        <div class="dropzone-previews"></div>
                        <fieldset>
                        <label> # K Clusters: </label> 
                        <select name="K">
			  <option>3</option>
			  <option>4</option>
			  <option>5</option>
                        </select>
                        <br>


                        <label> # expected Bands: </label> 
                        <input type="text" name="Bands" value="14">
                        <br>
                        <button type="submit" id="gelsubmit" class="btn btn-success" method="POST">Submit!</button><br>
                        </fieldset>
                        </form>
			
                         <div id="downloads">		
	   
			</div>
 			  
			  
		    </div>
		  </div>
		</div>
		
	</div>
  
</div> <!-- /container -->



{% end %}

{% block script %}
    <script src="static/js/index.js"></script>
{% end %}
