
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.urls import reverse 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from customadmin.forms import UserRegistrationForm
from menu.models import *
from home.models import *
from customadmin.forms import *
from django.shortcuts import get_object_or_404
# Create your views here.
class RegisterView(SuccessMessageMixin, CreateView):
    template_name= 'home_folder/register.html'
    success_url= reverse_lazy('login')
    form_class= UserRegistrationForm
    
    success_message='Your Profile was Created Successfully'

class LoginLogic(LoginView):
    template_name = "home_folder/login.html"

    
    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy('dashboard')
        return reverse_lazy('index')

class DashBoardView(ListView):
    model= CartItem
    template_name="home_folder/dashboard_index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_orders"] = CartItem.objects.all()
        if self.request.user.is_authenticated:
            context["user"]=self.request.user
        else:
            context["user"]="Guest"
        return context
    
        
class CartItemDB(ListView):
    model= CartItem
    template_name="home_folder/cartitems_db.html"

    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["all_orders"]=CartItem.objects.all()
        context["form"]= UpdateMessageForm
        return context


class UpdateMessage(UpdateView):
    model = CartItem
    form_class = UpdateMessageForm
    template_name = "home_folder/cartitems_db.html"
    success_url = reverse_lazy('cartitems_dashboard')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(CartItem, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_item'] = self.get_object()
        print(context['cart_item'].pk)
        return context

class ReviewDB(ListView):
    model= Review
    template_name= 'home_folder/review_db.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['reviews']= Review.objects.all()
        context['form']=UpdateReviewForm
        return context

class ReviewUpdateDB(UpdateView):
    model = Review
    form_class = UpdateReviewForm
    template_name = "home_folder/review_db.html"
    success_url = reverse_lazy('review_dashboard')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Review, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.get_object()
        return context

class ReviewDeleteDB(DeleteView):
    model=Review
    template_name="home_folder/delete.html"
    success_url= reverse_lazy('dashboard')



class BlogsViewDB(ListView):
    model= BlogDetails
    template_name='home_folder/blogs_db.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = BlogDetails.objects.all()
        context['form']=  BlogUpdateForm
        return context
    
class BlogUpdateViewDB(UpdateView):
    model= BlogDetails
    form_class= BlogUpdateForm
    template_name= 'home_folder/blogs_db.html'
    success_url= reverse_lazy('blog_dashboard')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(BlogDetails, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = self.get_object()
        return context

class BlogDeleteDB(DeleteView):
    model=BlogDetails
    template_name="home_folder/delete.html"
    success_url= reverse_lazy('blog_dashboard')

    





    
