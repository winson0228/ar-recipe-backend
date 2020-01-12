from graphene import Field, String
from django.db.models import Q
import requests
import os
import json
from .inputs import *
from .node import *
import base64
from .models import *

AZURE_API = "https://imagerecognitionnwhacks.cognitiveservices.azure.com/"

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
        print(analysis)

        tags = analysis['tags']
        name = 'Not an ingredient'
        confidence = 0.75
        for tag in tags:
            ingredient = Ingredients.objects.filter(name__icontains=tag['name']).first()
            if ingredient is not None:
                name = ingredient.name
                confidence = round(tag['confidence'], 2)
                break
        caption = analysis['description']['captions'][0]['text']

        new_obj = f'name={name},confidence={str(confidence)},caption={caption}'
        return AzureAI(name=new_obj)
