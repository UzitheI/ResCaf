from typing import Any
from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
            return self.name



class CartItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=None, null=True)
    dish=models.ForeignKey('Dish',on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    date_added=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.quantity} x {self.dish.name}'