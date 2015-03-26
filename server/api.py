__author__ = 'mpetyx'

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .pyapi import API


@csrf_exempt
def transform(request):

    if request.method == 'POST' or request.method == 'GET':


        # api = request.POST.get('api','')
        # location = request.POST.get('location','')
        # original_format = request.POST.get('original_format','')
        # to_format = request.POST.get('to_format','')

        location = "http://imagine.epu.ntua.gr:1988/api/doc/schema/Account/"
        original_format = "swagger"
        to_format = "raml"
        api = "123"

        api_framework = API()

        api_framework.parse(location=location, language=original_format)

        api_framework.serialise(to_format)


        if not api:
            return HttpResponse({"Please provide a Valid API!!"},status=401)
        else:
            return HttpResponse(api_framework.serialise(to_format),status=201)

    else:
        return HttpResponse(status=405)