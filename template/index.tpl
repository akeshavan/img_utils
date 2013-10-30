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


    </style>

{% end %}

{% block body %}
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

    <div class="container" ng-controller="IndexCtrl">

    <div class="jumbotron">
    <h1>TIF converter</h1>
    Drag and Drop your .tif files to convert them to high quality JPEGs
    <p>For the Douglas Lab at UCSF, to convert Typhoon .tif images</p>

    </div>
    <div class="row">
      <div class="span10">
      <form action="/file-upload"
      class="dropzone dz-clickable"
      enctype="multipart/form-data"
      id="my-awesome-dropzone"></form>
      </div>
    </div>

    <div class="row">
    <div class="span4" id="chat">
    
    </div>
    </div>

    </div> <!-- /container -->
{% end %}

{% block script %}
    <script src="static/js/index.js"></script>
{% end %}
