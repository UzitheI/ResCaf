from django.conf import settings
from django.urls import path,include
from .views import * 
from django.contrib.auth.views import *
from customadmin.views import LoginLogic
from django.conf.urls.static import static
from django.urls import reverse
from django.contrib.auth import views as auth_views 





urlpatterns = [
    path('login/', LoginLogic.as_view(template_name="home_folder/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
    path('dashboard/cart_items',CartItemDB.as_view(),name="cartitems_dashboard"),
    path('dashboard/cart_items/<int:pk>/', UpdateMessage.as_view(), name="messageUpdate"),
    path('dashboard/reviews',ReviewDB.as_view(),name='review_dashboard'),
    path('dashboard/review_update/<int:pk>/',ReviewUpdateDB.as_view(),name='review_update'),
    path('dashboard/review_delete/<int:pk>/',ReviewDeleteDB.as_view(),name='review_delete'),
    path('dashboard/blogs',BlogsViewDB.as_view(),name='blog_dashboard'),
    path('dashboard/blog_update/<int:pk>/',BlogUpdateViewDB.as_view(),name='blog_update'),
    path('dashboard/blog_delete/<int:pk>/',BlogDeleteDB.as_view(),name='blog_delete'),
    path('admin_register/',AdminRegisterView.as_view(),name='admin_register'),
    path('admin-login/',AdminLoginView.as_view(), name= 'admin_login'),
    path('admin-logout/', LogoutView.as_view(next_page= reverse_lazy('admin_login')), name='admin_logout'),
    path('reset-password',auth_views.PasswordResetView.as_view(template_name='home_folder/password_reset.html'),name='reset_password'),
    path('reset-password-sent',auth_views.PasswordResetDoneView.as_view(template_name='home_folder/password_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='home_folder/password_form.html'),name='password_reset_confirm'),
    path('reset-password-complete',auth_views.PasswordResetCompleteView.as_view(template_name='home_folder/password_done.html'),name='password_reset_complete'),
        

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 