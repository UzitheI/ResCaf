from django import forms
from . models import Dish, CartItem


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
    