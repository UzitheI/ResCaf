from django import forms
from . models import Dish, CartItem, UserSuggestions


class DishForm(forms.ModelForm):
    class Meta:
        model=Dish 
        fields='__all__'

    def __init__(self,*args,**kwargs):
        super(DishForm,self).__init__(*args,**kwargs)
        self.fields['country_of_origin'].empty_label="SELECT"

class searchForm(forms.Form): 
    query=forms.CharField(label='Search')

class cartForm(forms.ModelForm):
    class Meta:
        model= CartItem
        fields=['quantity']

class UserSuggestionsForm(forms.ModelForm):
    name = forms.CharField(label='What is the name of your dish?')
    description = forms.CharField(label='Describe your dish', widget=forms.Textarea)
    price = forms.FloatField(label='Price of the dish (in $)')
    image = forms.CharField(label='URL of the dish image')

    class Meta:
        model = UserSuggestions
        fields = ['name','description','price','image']
    
    
