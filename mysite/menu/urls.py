from django.urls import reverse_lazy, include, path
from . import views 

urlpatterns = [
    path('createDish',views.AddDish.as_view(),name='createDish'),
    path('search/', views.SearchListView.as_view(), name="search_view" )
]
