from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Cuisine(models.Model):
    name=models.CharField(unique=True,max_length=255)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=100,unique=True)
    price=models.FloatField()
    alcohol_content=models.BooleanField()
    description=models.CharField(max_length=255)
    ordered_on=models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("model_detail", args=[self.slug])

    class Meta:
        ordering= ['-ordered_on']

    def __str__(self):
        return self.name   
 

class Italian(Cuisine):
    pass

class Client(models.Model):
    client_name=models.CharField(max_length=100)
    ordered_dish=models.ManyToManyField(Cuisine)
    client_email=models.EmailField(max_length=254,null=True)
    


