from django.shortcuts import render
from requests import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from rest_framework.schemas.openapi import AutoSchema
from .models import HouseBase
from .serializers import HouseBaseSerializer, PredizerPriceHouse
from pycaret.regression import *
import pandas as pd


class BaseAPIView(generics.ListCreateAPIView):
    """

    API de consulta.


    """
    queryset = HouseBase.objects.all()
    serializer_class = HouseBaseSerializer

class PredictAPIView(APIView):
    """

    API da predict - house price.


    """
    serializer_class = PredizerPriceHouse
    def post(self,request):
        
        serializer = PredizerPriceHouse(data=request.data)
        #self.schema = AutoSchema.get_components(PredictSerializer.Meta.fields)
        serializer.is_valid(raise_exception=True)
        modelo = load_model('model')
        dados_entrada = pd.DataFrame(
            [
                serializer.data['status'],
                serializer.data['bed'],
                serializer.data['bath'],
                serializer.data['acre_lot'],
                serializer.data['city'],
                serializer.data['state'],
                serializer.data['zip_code'],
                serializer.data['house_size'],
            ]
        ).transpose()
        dados_entrada.columns = [
            "status",
            "bed",
            "bath",
            "acre_lot",
            "city",
            "state",
            "zip_code",
            "house_size"
        ]
        pred = predict_model(modelo, data=dados_entrada)

        resposta_dict = {
            "price": pred['Label']
        }
        return Response(resposta_dict, status=201)
