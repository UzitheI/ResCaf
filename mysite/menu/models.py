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
    total_amount = models.FloatField(default=0.0)
    message=models.CharField(max_length=200 ,default="Please Wait! We are processing your Order")
    is_accepted= models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
    

class UserSuggestions(models.Model):
    name= models.CharField(max_length=200)
    description=models.TextField()
    price=models.FloatField()
    image=models.CharField(max_length=200)
    user= models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    accepted= models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
