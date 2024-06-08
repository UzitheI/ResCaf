from django import forms 
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm
from menu.models import CartItem

class UserRegistrationForm( UserCreationForm):
    model= User, AbstractUser
    fields= '__all__'


class UpdateMessageForm(forms.ModelForm):
    
    class Meta:
        model = CartItem
        fields = ("message","is_accepted")
        labels= {'message': 'Enter a Message With the Decision'}




