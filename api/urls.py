from django.urls import path


from .views import BaseAPIView


urlpatterns = [
    path('housebase/',BaseAPIView.as_view(),name='housebase'),
]