from django.urls import path


from .views import BaseAPIView, PredictAPIView


urlpatterns = [
    path('housebase/',BaseAPIView.as_view(),name='housebase'),
    path('predictprice/',PredictAPIView.as_view(),name='predictprice'),

]