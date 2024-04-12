from django.urls import reverse_lazy, include, path
from . views import MenuView, AddDish, UpdateDish, DeleteDish
from . import views

urlpatterns = [
    path('createDish',AddDish.as_view(),name='createDish'),
    path('',MenuView.as_view(),name='menu'),
    path('updateDish/<int:pk>/', UpdateDish.as_view(), name='updateDish'),
    path('deleteDish/<int:pk>/', DeleteDish.as_view(), name='deleteDish'),
]
