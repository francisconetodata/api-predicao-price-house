from pyexpat import model
from django.db import models

# Create your models here.

class HouseBase(models.Model):
    status = models.CharField(
        'status',
        max_length=20,
        choices= (
            ('for_sale','for_sale'),
            ('ready_to_build','ready_to_build')
        )
    )
    price = models.FloatField(
        'price'
    )
    bed = models.IntegerField(
        'bed'
    )
    bath = models.IntegerField(
        'bath'
    )
    acre_lot = models.FloatField(
        'acre_lot'
    )
    full_address = models.TextField(
        'full_address'
    )
    street = models.TextField(
        'street'
    )
    city = models.CharField(
        'city',
        max_length=50
    )
    state = models.CharField(
        'state',
        max_length=10
    )
    zip_code = models.FloatField(
        'zip_code'
    )
    house_size = models.FloatField(
        'house_size'
    )
    sold_date = models.DateField(
        'sold_date'
    )