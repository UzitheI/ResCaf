from django.urls import path 
from . import views


urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('menu',views.MenuView.as_view(),name='menu'),
    path('about',views.AboutView.as_view(),name='about'),
    path('chef',views.ChefView.as_view(),name='chef'),
    path('contact',views.ContactView.as_view(),name='contact'),
    path('reservation',views.ReservationView.as_view(),name='reservation'),
    path('gallery',views.GalleryView.as_view(),name='gallery'),
    path('blog',views.BlogView.as_view(),name='blog'),
    path('order',views.OrderCreateView.as_view(),name='order'),
    path('list',views.listView.as_view(),name='list'),
    path('<int:pk>/',views.OrderUpdateView.as_view(),name='customer_update'),
    path('delete/<int:pk>/',views.OrderDeleteView.as_view(),name='customer_delete'),
]


