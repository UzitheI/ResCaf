from django import forms 
from .models import Cuisine,BookATable

class OrderForm(forms.ModelForm):
    
    class Meta:
        model=Cuisine
        fields=['customer_name','cuisine_name','customer_phone','price','alcohol_content','description','ordered_on']
    
class BookingForm(forms.ModelForm):
    class Meta:
        model=BookATable
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default time value for the time field
        self.fields['dateOfBooking'].initial = '2024-04-02 09:00:00'