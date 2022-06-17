from django.shortcuts import render
from requests import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from rest_framework.schemas.openapi import AutoSchema
from .models import HouseBase
from .serializers import HouseBaseSerializer, PredizerPriceHouse



class BaseAPIView(generics.ListCreateAPIView):
    """

    Fonte: https://www.kaggle.com/competitions/titanic
    E-mail: francisconetodata@gmail.com


    """
    queryset = HouseBase.objects.all()
    serializer_class = HouseBaseSerializer