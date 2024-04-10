
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
class RegisterView(SuccessMessageMixin, CreateView):
    template_name= 'home_folder/register.html'
    success_url= reverse_lazy('login')
    form_class= UserRegistrationForm
    
    success_message='Your Profile was Created Successfully'
