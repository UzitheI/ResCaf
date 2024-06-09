from django.urls import path 
from . import views
from django.conf.urls import static
from django.conf import settings


urlpatterns = [
    path('reservation',views.ReservationView.as_view(),name='reservation'),
    path('',views.IndexView.as_view(), name="index"),
    path('reservationUpdate/<int:pk>/',views.ReservationUpdate.as_view(),name='reservationUpdate'),
    path('reservationDelete/<int:pk>/',views.ReservationDelete.as_view(),name='reservationDelete'),
    path('review',views.ReviewView.as_view(),name="review"),
    path('reviewUpdate/<int:pk>/',views.ReviewUpdateView.as_view(),name="review_update"),
    path('reviewDelete/<int:pk>/',views.ReviewDelete.as_view(),name="review_delete"),
    path('blog',views.BlogView.as_view(), name="blog"),
    path('blogUpdate/<int:pk>/',views.BlogUpdateView.as_view(),name="blog_update"),
    path('blogDelete/<int:pk>/',views.BlogDeleteView.as_view(),name="blog_delete"),
    path('baseView',views.BaseView.as_view(),name="base_cart"),
]


