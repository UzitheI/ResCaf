from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Cuisine(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=255)
    customer_phone=models.CharField(max_length=244)
    cuisine_name=models.CharField(max_length=245)
    price=models.FloatField()
    alcohol_content=models.BooleanField()
    description=models.CharField(max_length=255)
    ordered_on=models.DateField(default=timezone.now)

class customer_details(models.Model):
    customer_id=models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name='cuisine_id')
    customer_name = models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name='cuisine_customer_name')
    customer_phone = models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name='cuisine_customer_phone')


class BookATable(models.Model):
    name=models.CharField(max_length=233)
    customer_email=models.EmailField()
    numberOfPeople=models.IntegerField()
    dateOfBooking=models.DateTimeField()




