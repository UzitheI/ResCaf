from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class BookATable(models.Model):
    name=models.CharField(max_length=233)
    customer_email=models.EmailField()
    numberOfPeople=models.IntegerField()
    dateOfBooking=models.DateTimeField()

class ChefDetails(models.Model):
    name=models.CharField(max_length=244)
    position=models.CharField(max_length=244)
    description=models.CharField(max_length=244)
    image=models.CharField(max_length=244)
    facebook=models.CharField(max_length=244)
    twitter=models.CharField(max_length=244)
    pinterest=models.CharField(max_length=244)
    linkedin=models.CharField(max_length=244)
    
# class Reviews(models.Model):
#     rating=models.FloatField()
#     title=models.CharField(max_length=244)
#     Description=models.CharField(max_length=244)


class BlogDetails(models.Model):
    title=models.CharField(max_length=224)
    description=models.CharField(max_length=224)
    header_image=models.CharField(max_length=224)
    writer=models.CharField(max_length=224)
    date=models.DateField(default=timezone.now)
