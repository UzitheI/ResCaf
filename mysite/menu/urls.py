from django.urls import reverse_lazy, include, path
from . import views

app_name = 'menu'
urlpatterns = [
    path('createDish',views.AddDish.as_view(),name='createDish'),
    path('menuList',views.MenuView.as_view(),name='menuList'),
    path('updateDish/<int:pk>/',views.UpdateDish.as_view(), name='updateDish'),
    path('deleteDish/<int:pk>/', views.DeleteDish.as_view(), name='deleteDish'),
    path('addtoCart/<int:dish_id>/', views.AddToCartView.as_view(), name="addtoCart"),
    path('remove/<int:pk>/', views.RemoveFromCart.as_view(), name='remove_from_cart'),
    path('quantityUpdate/<int:item_id>/', views.QuantityUpdateView.as_view(), name='quantityUpdate'),
    path('view_cart', views.CartView.as_view(), name='view_cart'),
    path('error', views.ErrorView.as_view(), name="error"),
    path('suggestions',views.AddSuggestions.as_view(), name="addsuggestions"),
    path('suggUpdate/<int:pk>/',views.SuggestionUpdateView.as_view(),name="sugg_update"),
    path('suggDelete/<int:pk>/',views.SuggestionDeleteView.as_view(),name="sugg_delete"),
    # path('viewAllOrders',views.ViewAllCartItems.as_view(),name="viewAllCartItems"),
]
