from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request):
    # """"
    # GET METHOD
    # """"
    # instance = Product.objects.last()

    # data = {}

    # if instance:
    #     #     data = model_to_dict(instance, fields=['title', 'content'])
    #     # else:
    #     #     pass
    #     data = ProductSerializer(instance).data
    # """""
    # POST METHOD
    # """

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):

        print(serializer.data)
        

        return Response(serializer.data)
