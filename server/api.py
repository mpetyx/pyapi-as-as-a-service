__author__ = 'mpetyx'

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from pyapi import API
import logging
import requests


@csrf_exempt
def transform(request):

    if request.method == 'POST' or request.method == 'GET':


        # api = request.POST.get('api','')
        location = request.GET.get('location','')
        original_format = request.GET.get('original_format','')
        to_format = request.GET.get('to_format','')

        # location = "http://imagine.epu.ntua.gr:1988/api/doc/schema/Account/"
        # original_format = "swagger"
        # to_format = "raml"
        # api = "123"

        api_framework = API()

        api_framework.parse(location=location, language=original_format)

        api_framework.serialise(to_format)


        if not location:
            return HttpResponse({"Please provide a Valid API!!"},status=401)
        else:
            return HttpResponse(api_framework.serialise(to_format),status=201)

    else:
        return HttpResponse(status=405)

@csrf_exempt
def openi(request):

    if request.method == 'POST' or request.method == 'GET':

        openi_server_url = "http://imagine.epu.ntua.gr:1988/api/doc/resources/"
        openi_server_url = "http://api-builder.tools.epu.ntua.gr/web/api-docs/Core/api-docs.json"
        schema = "http://api-builder.tools.epu.ntua.gr/web/api-docs/Core"



        server = requests.get(openi_server_url)

        objects = server.json()['apis']

        apis = []

        api_framework = API()
        to_format = request.GET.get('to_format','')

        for object in objects:
            logging.info("Accessing Object:   "+str(schema+object['path']))
            api_framework.parse(location=schema+object['path'], language="swagger")

            apis.append(api_framework.serialise(to_format))



        return HttpResponse(apis,status=201)

    else:
        return HttpResponse(status=405)