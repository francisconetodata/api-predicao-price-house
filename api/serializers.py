from rest_framework import serializers

from .models import HouseBase


class HouseBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseBase

class PredizerPriceHouse(serializers.ModelSerializer):
    class Meta:
        model = HouseBase
        fields = (
            "status",
            "bed",
            "bath",
            "acre_lot",
            "city",
            "state",
            "zip_code",
            "house_size"
        )