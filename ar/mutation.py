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
        name = 'Not an ingredient|'
        confidence = 0.75
        max_confidence = 0
        for tag in tags:
            ingredients = Ingredients.objects.filter(name__icontains=tag['name'])
            temp = round(tag['confidence'], 2)
            if ingredients is not None and temp > max_confidence:
                name = ''
                for ingredient in ingredients:
                    name += ingredient.name + '|'
                max_confidence = temp
        name = name[:-1]
        if max_confidence != 0:
            confidence = round(max_confidence, 2)
        caption = analysis['description']['captions'][0]['text']

        new_obj = f'name={name},confidence={str(confidence)},caption={caption}'
        return AzureAI(name=new_obj)
