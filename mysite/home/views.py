
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from . models import BookATable, ChefDetails, BlogDetails, Table
from .forms import BookingForm, ReviewForm, BlogForm
from django.urls import reverse_lazy
from menu.models import Dish
from home.models import Review
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from home.views import BookATable
from home.models import *
from menu.models import *

class BaseView(LoginRequiredMixin,ListView):
    model= CartItem
    template_name= "home_folder/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = CartItem.objects.filter(user=self.request.user)
        print(context['cart_items'])
        context['total_price'] = sum(item.dish.price * item.quantity for item in context['cart_items'])
        return context
     

class IndexView(CreateView, LoginRequiredMixin):
    template_name='home_folder/index.html'
    model = BookATable
    form_class = BookingForm
    template_name = "home_folder/index.html"
    success_url = reverse_lazy('reservation')

    def get_queryset(self):
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dishes']= Dish.objects.all()
        context["chefs"] = ChefDetails.objects.all()
        context["blogs"]= BlogDetails.objects.filter(is_approved=True)
        context["reviews"]=Review.objects.all()
        if self.request.user.is_authenticated:
            context["user"]= self.request.user
        else: 
            context["user"]='guest'
            logout(self.request)
        return context
    
    def form_valid(self, form):
        formi = form.instance
        formi.user= self.request.user
        formi.table.is_available = False
        formi.save()
        return super().form_valid(form)

class ReviewView(LoginRequiredMixin,CreateView):
    model=Review
    form_class= ReviewForm
    template_name= "home_folder/review.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_reviews'] = Review.objects.filter(user=self.request.user)
        return context

class ReviewUpdateView(UpdateView):
    model=Review
    form_class=ReviewForm
    template_name="home_folder/review.html"
    success_url=reverse_lazy('review')

class ReviewDelete(DeleteView):
    model=Review
    template_name="home_folder/delete.html"
    success_url= reverse_lazy('review')

class ReservationView(LoginRequiredMixin, CreateView):
    model = BookATable
    form_class = BookingForm
    template_name = 'home_folder/reservation.html'
    success_url = reverse_lazy('reservation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tables'] = Table.objects.filter(is_available=True)
        context['bookings'] = BookATable.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        formi = form.instance
        formi.user= self.request.user
        formi.is_available = False
        formi.save()
        return super().form_valid(form)

class ReservationUpdate(UpdateView):
    model= BookATable
    form_class= BookingForm
    template_name= 'home_folder/reservation.html'
    success_url= reverse_lazy('reservation')

class ReservationDelete(DeleteView):
    model= BookATable
    template_name="home_folder/delete.html"
    success_url= reverse_lazy('reservation')


class BlogView(LoginRequiredMixin, CreateView):
    model = BlogDetails
    form_class = BlogForm
    template_name = "home_folder/blog.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = BlogDetails.objects.filter(writer_name=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.writer_name = self.request.user
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model=BlogDetails
    form_class= BlogForm
    template_name="home_folder/blog.html"
    success_url= reverse_lazy('blog')

class BlogDeleteView(DeleteView):
    model= BlogDetails
    template_name="home_folder/delete.html"
    success_url= reverse_lazy('blog')
    