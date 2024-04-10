from django import forms 
from .models import BookATable

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
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default time value for the time field
        self.fields['dateOfBooking'].initial = '2024-04-02 09:00:00'