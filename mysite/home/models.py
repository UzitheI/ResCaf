from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from menu.models import Dish





class Table(models.Model):
    table_number=models.IntegerField()
    table_price=models.FloatField()
    table_description= models.TextField()
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return str(self.table_number)
    

class BookATable(models.Model):
    name=models.CharField(max_length=233)
    customer_email=models.EmailField()
    numberOfPeople=models.IntegerField()
    dateOfBooking=models.DateTimeField(default=timezone.now)
    table=models.ForeignKey(Table,on_delete=models.CASCADE, default=None)
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.dateOfBooking)

class ChefDetails(models.Model):
    name=models.CharField(max_length=244)
    position=models.CharField(max_length=244)
    description=models.CharField(max_length=244)
    image=models.CharField(max_length=244)
    facebook=models.CharField(max_length=244)
    twitter=models.CharField(max_length=244)
    pinterest=models.CharField(max_length=244)
    linkedin=models.CharField(max_length=244)

    def __str__(self):
        return str(self.name)
    
# class Reviews(models.Model):
#     rating=models.FloatField()
#     title=models.CharField(max_length=244)
#     Description=models.CharField(max_length=244)


class BlogDetails(models.Model):
    title=models.CharField(max_length=224)
    description=models.CharField(max_length=224)
    header_image=models.CharField(max_length=224)
    writer_name=models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    date=models.DateField(default=timezone.now)
    is_approved= models.BooleanField(default=False )

    def __str__(self):
        return str(self.title)

class Review(models.Model):
    dish=models.ForeignKey(Dish,on_delete=models.CASCADE,default=None,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=None, null=True)
    date_time=models.DateTimeField(default=timezone.now)
    stars=models.FloatField()
    description=models.TextField()
    is_shown= models.BooleanField(default=False)

    def __str__(self):
        return str(self.description)




