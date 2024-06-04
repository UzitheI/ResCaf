from django.contrib import admin
from django.urls import path,include
from .views import * 
from django.contrib.auth.views import *
from customadmin.views import LoginLogic


urlpatterns = [
    path('login/', LoginLogic.as_view(template_name="home_folder/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),

]           