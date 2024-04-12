from django.urls import path 
from . import views


urlpatterns = [
    path('book',views.BookingView.as_view(),name='book'),
    path('reservation',views.ReservationView.as_view(),name='reservation'),
    path('',views.IndexView.as_view(), name="index"),
    path('table/<int:pk>/',views.TableUpdatView.as_view(),name='table_update'),

]


