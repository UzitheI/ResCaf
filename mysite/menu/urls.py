from django.urls import reverse_lazy, include, path
from . views import RemoveFromCart,MenuView, AddDish, UpdateDish, DeleteDish, AddToCartView, QuantityUpdateView, CartView, ErrorView
from . import views

app_name = 'menu'
urlpatterns = [
    path('createDish',AddDish.as_view(),name='createDish'),
    path('menuList',MenuView.as_view(),name='menuList'),
    path('updateDish/<int:pk>/', UpdateDish.as_view(), name='updateDish'),
    path('deleteDish/<int:pk>/', DeleteDish.as_view(), name='deleteDish'),
    path('addtoCart/<int:dish_id>/', AddToCartView.as_view(), name="addtoCart"),
    path('remove/<int:pk>/', RemoveFromCart.as_view(), name='remove_from_cart'),
    path('quantityUpdate/<int:item_id>/', QuantityUpdateView.as_view(), name='quantityUpdate'),
    path('view_cart', CartView.as_view(), name='view_cart'),
    path('error', ErrorView.as_view(), name="error")
]
