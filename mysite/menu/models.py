from typing import Any
from django.db import models

class Countries(models.Model):
    countries=models.CharField(max_length=100)

    def __str__(self):
        return self.countries
    
class Dish(models.Model):
    name= models.CharField(max_length=100)
    description=models.TextField()
    price=models.FloatField()
    image=models.CharField(max_length=200)
    country_of_origin=models.ForeignKey(Countries, on_delete=models.CASCADE)
