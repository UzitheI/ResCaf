from django import forms 
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm
from menu.models import *
from home.models import *
class UserRegistrationForm( UserCreationForm):
    model= User, AbstractUser
    fields= '__all__'


class UpdateMessageForm(forms.ModelForm):
    
    class Meta:
        model = CartItem
        fields = ("message","is_accepted")
        labels= {'message': 'Enter a Message With the Decision'}


class UpdateReviewForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea())
    class Meta:
        model= Review
        fields={'is_shown','description'}
        labels={'is_shown':'Do you want to show the review?', 'description':'Make changes in the description:'}


class BlogUpdateForm(forms.ModelForm):
    description= forms.CharField(widget=forms.Textarea(), max_length=250, required=False)    
    class Meta:
        model= BlogDetails
        fields={'title','description', 'header_image', 'is_approved'}
        label={'title':'Enter your title:', 'description':'Enter your description:', 'header_image':'Enter a suitable image:', 'is_approved':'Do you want the blog to appear?'}


