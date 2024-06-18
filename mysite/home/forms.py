from django import forms 
from .models import BookATable, Review, Table, BlogDetails
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from cked.widgets import CKEditorWidget
from django.contrib.admin.widgets import AdminRadioSelect
from .models import Review, RATING_CHOICES

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
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'customer_email':forms.TextInput(attrs={'class':'form-control'}),
            'numberOfPeople':forms.TextInput(attrs={'class':'form-control'}),
            'table':forms.Select(attrs={'class':'form-control'}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model=BlogDetails
        fields= ['title','description','header_image']


    
class ReviewForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    stars = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial=5.0,
    )

    class Meta:
        model = Review
        fields = ['dish', 'stars', 'description']
        widgets = {
            'dish': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }