from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from menu.models import CartItem

class UserRegistrationForm( UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User 
        fields= '__all__'


class UpdateMessageForm(forms.Form):
    message= forms.CharField( max_length=200, required=True, label="Enter your message:")

    class Meta:
        model= CartItem
        fields = ['message']



