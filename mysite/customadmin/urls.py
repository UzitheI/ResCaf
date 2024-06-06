from django.conf import settings
from django.urls import path,include
from .views import * 
from django.contrib.auth.views import *
from customadmin.views import LoginLogic
from django.conf.urls.static import static


urlpatterns = [
    path('login/', LoginLogic.as_view(template_name="home_folder/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
    path('dashboard/cart_items',CartItemDB.as_view(),name="cartitems_dashboard"),
    path('dashboard/cart_items/<int:pk>',UpdateMessage.as_view(), name= "message_update")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 