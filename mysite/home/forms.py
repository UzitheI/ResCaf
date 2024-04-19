from django import forms 
from .models import BookATable, Review, Table, BlogDetails

# class OrderForm(forms.ModelForm):
    
#     class Meta:
#         model=Cuisine
#         fields= '__all__'

#         def __init__(self,*args,**kwargs):
#             super(OrderForm,self).__init__(*args,**kwargs)
#             available_cuisines=AvailableCuisines.objects.all()
            
    
class BookingForm(forms.ModelForm):
    class Meta:
        model=BookATable
        fields=['name','customer_email','numberOfPeople','table']
        table = forms.ModelChoiceField(
        queryset=Table.objects.all(),
        empty_label="Check reservation for Table description",
        label="Table"
    )

class BlogForm(forms.ModelForm):
    class Meta:
        model=BlogDetails
        fields= ['title','description','header_image']


    
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['dish', 'stars' , 'description']