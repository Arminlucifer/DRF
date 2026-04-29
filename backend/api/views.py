from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
# Create your views here.


def api_home(request, *args, **kwargs):

    model_data = Product.objects.first()
    print(model_data.title)
    data = {}

    if model_data:
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    else:
        pass

    return JsonResponse(
        (data)
    )
