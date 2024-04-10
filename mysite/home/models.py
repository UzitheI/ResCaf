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




