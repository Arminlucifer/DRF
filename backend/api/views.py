from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.


def api_home(request):

    body = request.body
    data = {}

    try:
        data = json.loads(body)
    except:
        pass

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)

    return JsonResponse(
        (data)
    )
