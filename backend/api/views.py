from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request):

    instance = Product.objects.last()

    data = {}

    if instance:
        #     data = model_to_dict(instance, fields=['title', 'content'])
        # else:
        #     pass
        data = ProductSerializer(instance).data

    return Response(data)
