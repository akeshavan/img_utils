{% extends "base.tpl" %}

{% block head %}

<link href="/static/css/index.css" rel="stylesheet">
<link href="/static/css/mat.css" rel="stylesheet">


{% end %}

{% block body %}


<div class="container">

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
			  <p class="navbar-text pull-right">
			               Logged in as <a href="#" class="navbar-link"></a>
			             </p>
	            <ul class="nav">
	              <li class="active"><a href="/">Home</a></li>
	              <li><a href="#about">About</a></li>
	              <li><a href="/login">Login</a></li>
				  <li><a href="#" onClick="logout()">Logout</a></li>
	            </ul>
	          </div><!--/.nav-collapse -->
	        </div>
	      </div>
	    </div>
		
	<div class="row-fluid">
		<div class="tabbable tabs-left"> <!-- Only required for left/right tabs -->
		  <ul class="nav nav-tabs">
		    <li class="active"><a href="#home" data-toggle="tab">Home</a></li>
			<li><a href="#tif" data-toggle="tab">Tif Converter</a></li>
		    <li><a href="#gel" data-toggle="tab">Gel Analysis</a></li>
			<li><a href="#mat" data-toggle="tab">Mat Viewer</a></li>
			<li><a href="#wiki" data-toggle="tab">Wiki</a></li>
		  </ul>
		  
		  <div class="tab-content">
			  {% include home.tpl %}
			  {% include tif.tpl %}
			  {% include gel.tpl %}
			  {% include mat.tpl %}
			  {% include wiki.tpl %}

		  </div>
		</div>
		
	</div>
  
</div> <!-- /container -->



{% end %}

{% block script %}
    <script src="static/js/index.js"></script>
	<script src="static/js/tif.js"></script>
	<script src="static/js/gel.js"></script>
	<script>
	var logout = function(){
	document.location.href = "https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=http://localhost:8888";
	}</script>
	<script src="static/js/mat.js"></script>
	<script src="static/js/wiki.js"></script>
{% end %}
