from flask import Flask, request, redirect, jsonify, render_template, url_for
import os
from werkzeug.utils import secure_filename
import sys
from google.oauth2 import service_account

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

@app.route("/")
def index():
    return render_template('SkinCareSite.html')

@app.route("/SkinResult")
def SkinResult(request):
    return render_template('SkinResult.html', request)

@app.route("/Blog")
def Blog():
    return render_template("blog.html")

@app.route("/Contact")
def Contact():
    return render_template("contactus.html")

@app.route("/Register")
def Register():
    return render_template("register.html")

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":

        if request.files:
            image = request.files["image"].read()
            #print(image)
            content = bytes(image)
            #predict.get_prediction(content, "ruhacks-277409", "ICN529872245611298816")

            #with open("acnetest.jpg","rb") as image:
             #    f = image.read()
             #    b = bytearray(f)
            #a = bytes(b) 
            #predict.get_prediction(, "ruhacks-277409", "ICN529872245611298816") 
            result = get_prediction(content, "ruhacks-277409", "ICN2611098223409889280")
            print(result) 
            return render_template('SkinResult.html', request=result.payload[0].display_name)
            #return redirect(url_for('SkinResult'))
    return render_template('SkinCareSite.html')

def get_prediction(content, project_id, model_id):
  credentials = service_account.Credentials. from_service_account_file('visionAPI.json')
  prediction_client = automl_v1beta1.PredictionServiceClient(credentials=credentials)

  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {}
  request = prediction_client.predict(name, payload, params) 
  return request

if __name__ == '__main__':
    app.run(debug=False)