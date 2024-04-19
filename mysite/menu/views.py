from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView,  ListView, TemplateView, UpdateView, DeleteView, RedirectView
from . models import Dish, UserSuggestions
from .forms import DishForm,searchForm,cartForm, UserSuggestionsForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Dish, CartItem
from django.http import HttpResponseRedirect
import logging

logger = logging.getLogger(__name__)

class ErrorView(TemplateView):
    template_name="home_folder/error.html"

class AddSuggestions(LoginRequiredMixin, CreateView):
    form_class= UserSuggestionsForm
    template_name = 'home_folder/somethingelse.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user 
        context["usersuggestions"] = UserSuggestions.objects.filter(user=self.request.user)
        query = self.request.GET.get('q', '')
        if query:
            context['dishes'] = Dish.objects.filter(name__icontains=query)
        else:
            context['dishes'] = Dish.objects.all()
        context['query'] = query 
        return context

class SuggestionUpdateView(UpdateView):
    model= UserSuggestions
    form_class= UserSuggestionsForm
    template_name="home_folder/somethingelse.html"
    success_url = reverse_lazy('menu:addsuggestions')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usersuggestions'] = UserSuggestions.objects.filter(user=self.request.user)
        return context

class SuggestionDeleteView(DeleteView):
    model= UserSuggestions
    template_name= "home_folder/delete.html"
    success_url = reverse_lazy("menu:addsuggestions")
    
class AddDish(UserPassesTestMixin, CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'home_folder/alldish.html'
    success_url = reverse_lazy('menu:createDish')

    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('menu:addsuggestions')
        else:
            return super().handle_no_permission()

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
    template_name='home_folder/menu.html'

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

# class CartView(ListView):
#     model = CartItem
#     template_name = 'home_folder/cart.html'

#     def get_queryset(self):
#         return CartItem.objects.filter(user=self.request.user)

class RemoveFromCart(DeleteView):
    model=CartItem
    template_name="home_folder/delete.html"
    success_url=reverse_lazy('menu:view_cart')

class CartView(LoginRequiredMixin, CreateView):
    template_name = 'home_folder/cart.html'
    form_class = cartForm
    success_url = reverse_lazy('menu:view_cart')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = CartItem.objects.filter(user=self.request.user)
        context['total_price'] = sum(item.dish.price * item.quantity for item in context['cart_items'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class QuantityUpdateView(UpdateView):
    model = CartItem
    form_class = cartForm
    template_name = "home_folder/cart.html"
    success_url = reverse_lazy('menu:menuList')

    def get_object(self, queryset=None):
        return get_object_or_404(CartItem, id=self.kwargs['item_id'])
