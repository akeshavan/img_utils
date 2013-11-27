<div class="tab-pane" id="wiki" ng-controller="WikiCtrl">

    <div class="jumbotron">
    <h1>Wiki Image Upload</h1>
    Submit files to upload to the Wiki
    <p>For the Douglas Lab Wiki Notebook at UCSF</p>

    </div>

<form action="https://wiki.bionano.ucsf.edu/anisha/Special:Upload" method="post" class="form well" enctype="multipart/form-data" id="mw-upload-form">
	<fieldset>
		<legend>Source file</legend>

		<table id="mw-htmlform-source">
			<tbody>
				<tr class="mw-htmlform-field-UploadSourceField  ">
					<td class="mw-label">
						<label for="wpSourceTypeFile">Source filename:</label>
					</td>
					<td class="mw-input">
						<input id="wpUploadFile" name="wpUploadFile" size="60" type="file" class="upload"/>
					</td>
				</tr>

				<tr>
					<td colspan="2" class="htmlform-tip">Maximum file size: 100 MB  (a file on your computer)</td>
				</tr>

				<tr class="mw-htmlform-field-HTMLInfoField  ">
					<td class="mw-label"><label></label></td>
					<td class="mw-input">
						<div id="mw-upload-preferred">
							<p>Preferred file types: png, gif, jpg, jpeg, tar, gz, png, gif, jpg, jpeg, ogg, zip, ai, xls, doc, docx, py, pl, sh, tiff, bmp, txt, csv, pdf, ppt, key, mov, mpg, mpeg, avi, wmv, xvid, svg, svgz, json, ma, mb, xml, m.
							</p>
						</div>
						<div id="mw-upload-prohibited">
							<p>Prohibited file types: html, htm, js, jsb, mhtml, mht, xhtml, xht, exe, scr, dll, msi, vbs, bat, com, pif, cmd, vxd, cpl.
							</p>
						</div>

					</td>
				</tr>
			</tbody>
		</table>

	</fieldset>

	<input id="wpEditToken" type="hidden" value="0228d7952603fd4d278af148624f8730+\" name="wpEditToken" />
	<input type="hidden" value="Special:Upload" name="title" />
	<input id="wpDestFileWarningAck" name="wpDestFileWarningAck" type="hidden" />
	<input type="submit" value="Upload file" name="wpUpload" title="Start upload [s]" accesskey="s" class="btn btn-success" />

</form>


</div>
