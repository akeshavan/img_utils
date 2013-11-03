<div class="tab-pane" id="gel"  ng-controller="GelCtrl">
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

             <div id="geldownloads">		

             </div>
  
  
</div>