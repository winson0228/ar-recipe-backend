from graphene import Field, String
from django.db.models import Q
import requests
import os
import json
from .inputs import *
from .node import *
import base64

AZURE_API = "https://imagerecognitionnwhacks.cognitiveservices.azure.com/"
LIST_OF_INGREDIENTS = ["apple", "orange", "banana"]

class AzureAI(graphene.Mutation):
    class Arguments:
        input = String()

    name = String()

    def mutate(self, info, **data):
        image_data = base64.b64decode(data['input'])
        print(bytearray(image_data))
        analyze_url = AZURE_API + "vision/v2.1/analyze"
        headers = {'Ocp-Apim-Subscription-Key': os.environ.get('NWHACKS_SECRET_KEY'),'Content-Type': 'application/octet-stream'}
        params = {'visualFeatures': 'Tags,Description'}
        response = requests.post(analyze_url, headers=headers, params=params, data=bytearray(image_data))
        response.raise_for_status()

        analysis = response.json()

        tags = analysis['tags']
        name = ''
        confidence = 0
        for tag in tags:
            if tag['name'] in LIST_OF_INGREDIENTS:
                name = tag['name']
                confidence = tag['confidence']
                break;
        caption = analysis['description']['captions'][0]['text']

        new_obj = {
            "name": name,
            "confidence": confidence,
            "caption": caption
        }
        return AzureAI(name=new_obj)
