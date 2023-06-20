# this file explains it all


# https://developers.google.com/youtube/v3/docs/thumbnails/set?apix=true#params


import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload



# VIDEO_ID = '63MZ6Q6U5y8'
# thumbnail_path = './bg.jpg'
credentials_path = './client_secret.json'
scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']                      # https://developers.google.com/youtube/v3/guides/auth/installed-apps#identify-access-scopes


flow = InstalledAppFlow.from_client_secrets_file(credentials_path, scopes)        # Get credentials and create an API client
flow.run_local_server(host='localhost', port=8080)
credentials = flow.credentials

api_service_name = 'youtube'
api_version = 'v3'
youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

def update(VIDEO_ID,thumbnail_path,title,description):
  try:
      request = youtube.thumbnails().set(videoId=VIDEO_ID, media_body=MediaFileUpload(thumbnail_path))
      # request = youtube.videos().update(
      #     part="snippet,status,localizations",
      #     body={
      #       "id": VIDEO_ID,
      #       "localizations": {
      #         "es": {
      #           "title": title,
      #           "description": description
      #         }
      #       },
      #       "snippet": {
      #         "categoryId": 28,
      #         "defaultLanguage": "en",
      #         "description": description,
      #         "tags": [
      #           "qiqt","QIQT23","QIQT","Quantum information","Quantum Computing"
      #         ],
      #         "title": title
      #       }
      #     }
      # )
      response = request.execute()
      print(response)
  except Exception as ex:
      print(f'error: {ex}')


import json

# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
n=0
for i in data:
  n+=1
  if len(i["Name"]) > 88 :
      N = 100 - (12 + len(i["Name"])) - 3
      VIDEO_ID = (i["Link"])
      title = ('QIQT23 | ' + i['Name'] + ' - ' + i["Title"][0:N] + '...' )
      description = ("Please visit https://qiqt2023.org/ for more information \n \n Speaker:" + i["Name"] + " - " + i["Affiliation"]  + "\n \n Abstract:" + i["Abstract"])
      thumbnail_path = ('./thumbnails/'+i["Image name"])
  else:
    N = len(i["Title"])
    VIDEO_ID = (i["Link"])
    title = ('QIQT23 | ' + i['Name'] + ' - ' + i["Title"][0:N] )
    description = ("Please visit https://qiqt2023.org/ for more information \n \nSpeaker:" + i["Name"] + " - " + i["Affiliation"] + "\n \nAbstract:" + i["Abstract"])
    thumbnail_path = ('./thumbnails/'+i["Image name"]+".png")
  update(VIDEO_ID,thumbnail_path,title,description)
  print(n)

# Closing file
f.close()
