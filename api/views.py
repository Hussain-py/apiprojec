from django.shortcuts import render
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from google_play_scraper import app
# Create your views here.
#



class data(APIView):
    def get(self,request):
        name = request.query_params.get("Name")
        result = app(
            name,
            lang='en', #default to 'en'
            country='us' #default to 'us
        )
        y = json.dumps(result)
        return  Response(y)
    def post(self):
        pass
