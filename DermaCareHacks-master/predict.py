import sys
from google.oauth2 import service_account

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2


# 'content' is base-64-encoded image data.
def get_prediction(content, project_id, model_id):
  credentials = service_account.Credentials. from_service_account_file('visionAPI.json') #why is there a space tho. 
  prediction_client = automl_v1beta1.PredictionServiceClient(credentials=credentials)

  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {}
  request = prediction_client.predict(name, payload, params)
  #print("HELLOOOOO")
  #print(request)
  return request  # waits till request is returned
  
if __name__ == '__main__':
  file_path = sys.argv[1] 
  project_id = sys.argv[2]
  model_id = sys.argv[3]

  with open(file_path, 'rb') as ff:
    content = ff.read()


  result = get_prediction(content, project_id, model_id)
  print(result) 
  #classification = result.classification.score

  #print(result.payload)
  #print(result.payload[0].display_name)
  #print(result.payload[0].classification.score)

  
 # pip3 install google-cloud-automl
 # python3 predict.py lymetest.jpg ruhacks-277409 ICN5194194084683579392