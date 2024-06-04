from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from customadmin.forms import UserRegistrationForm

# Create your views here.
class RegisterView(SuccessMessageMixin, CreateView):
    template_name= 'home_folder/register.html'
    success_url= reverse_lazy('login')
    form_class= UserRegistrationForm
    
    success_message='Your Profile was Created Successfully'

class LoginLogic(LoginView):
    template_name = "home_folder/login.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy('dashboard')
        return reverse_lazy('index')

class DashBoardView(TemplateView):
    template_name="home_folder/dashboard_index.html"


    
