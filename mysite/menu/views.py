from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView,  ListView, TemplateView, UpdateView, DeleteView, RedirectView
from . models import Dish
from .forms import DishForm,searchForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dish, CartItem
from django.http import HttpResponseRedirect
import logging

logger = logging.getLogger(__name__)

class ErrorView(TemplateView):
    template_name="home_folder/error.html"
class AddDish(CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'home_folder/alldish.html'
    success_url = reverse_lazy('menu:createDish')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if query:
            context['dishes'] = Dish.objects.filter(name__icontains=query)
        else:
            context['dishes'] = Dish.objects.all()

        context['query'] = query

        return context
        
class UpdateDish(UpdateView):
    model=Dish 
    form_class=DishForm
    template_name="home_folder/alldish.html"
    success_url= reverse_lazy('menu:createDish')

class DeleteDish(DeleteView):
    model=Dish
    template_name="home_folder/delete.html"
    success_url=reverse_lazy('menu:createDish')

class MenuView(ListView):
    model= Dish
    template_name='home_folder/menu-1.html'

    def get_context_data(self, **kwargs):
        context= super(). get_context_data(**kwargs)
        context['dishes']=self.get_queryset()
        return context  

class AddToCartView(View):
    def post(self, request, dish_id):
        dish = Dish.objects.get(id=dish_id)
        cart_item, created = CartItem.objects.get_or_create(
            dish=dish, 
            user=request.user,
            defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('menu:view_cart')

class CartView(ListView):
    model = CartItem
    template_name = 'home_folder/cart.html'

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

class RemoveFromCart(DeleteView):
    model=CartItem
    template_name="home_folder/delete.html"
    success_url=reverse_lazy('view-cart')

# class CartView(LoginRequiredMixin, TemplateView):
#     template_name = 'home_folder/cart.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_cart, created = CartItem.objects.get_or_create(user=self.request.user)
#         context['cart_items'] = user_cart
#         return context
    
#     def post(self, request, *args, **kwargs):
#         return self.get(request, *args, **kwargs)