from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from . models import BookATable
from .forms import BookingForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# def index(request):
#     return render(request,'home_folder/index.html')

class IndexView(CreateView):
    model=BookATable
    form_class=BookingForm
    template_name='home_folder/index.html'
    success_url=reverse_lazy('table')

# deSCADE)f employee_list(request):
#     context = {'employee_list' :Employee.objects.all()}
#     return render(request,"employee_register/employee_list.html",context)

class MenuView(TemplateView):
    template_name='home_folder/menu-1.html'
    
class AboutView(TemplateView):
    template_name='home_folder/about.html'

class ChefView(TemplateView):
    template_name='home_folder/chef.html'

class ContactView(TemplateView):
    template_name='home_folder/contact.html'

class ReservationView(TemplateView):
    template_name= 'home_folder/reservation.html'

class GalleryView(TemplateView):
    template_name='home_folder/gallery-grid-2-colum.html'

class BlogView(TemplateView):
    template_name='home_folder/blog-single.html'
  # Assuming Cuisine is your custom model

# class listView(ListView):
#     model=Cuisine
#     template_name = 'home_folder/list.html'
#     context_object_name='cuisine_list'
    
# class TableView(ListView):
#     model=Cuisine
#     template_name = 'home_folder/table.html'
#     context_object_name='client_table'
    


# class OrderCreateView(CreateView):
#     model=Cuisine
#     form_class=OrderForm
#     template_name='home_folder/place_your_order.html'
#     success_url=reverse_lazy('list')

# class OrderUpdateView(UpdateView):
#     model=Cuisine
#     form_class=OrderForm
#     template_name='home_folder/place_your_order.html'
#     success_url=reverse_lazy('list')

# class OrderDeleteView(DeleteView):
#     model=Cuisine
#     success_url=reverse_lazy('list')
#     template_name="home_folder/cuisine_confirm_delete.html"


#     def get_object(self):
#         """Override get_object to get the specific employee instance."""
#         pk = self.kwargs.get('pk')
#         return Cuisine.objects.get(pk=pk)class listView(ListView):
#     model=Cuisine
#     template_name = 'home_folder/list.html'
#     context_object_name='cuisine_list'
    
# class TableView(ListView):
#     model=Cuisine
#     template_name = 'home_folder/table.html'
#     context_object_name='client_table'
    


# class OrderCreateView(CreateView):
#     model=Cuisine
#     form_class=OrderForm
#     template_name='home_folder/place_your_order.html'
#     success_url=reverse_lazy('list')

# class OrderUpdateView(UpdateView):
#     model=Cuisine
#     form_class=OrderForm
#     template_name='home_folder/place_your_order.html'
#     success_url=reverse_lazy('list')

# class OrderDeleteView(DeleteView):
#     model=Cuisine
#     success_url=reverse_lazy('list')
#     template_name="home_folder/cuisine_confirm_delete.html"


#     def get_object(self):
#         """Override get_object to get the specific employee instance."""
#         pk = self.kwargs.get('pk')
#         return Cuisine.objects.get(pk=pk)

class TableUpdatView(UpdateView):
    model=BookATable
    form_class=BookingForm
    template_name="home_folder/index.html"
    success_url=reverse_lazy('tablelist')

# class TableDeleteView(DeleteView):

# def employee_form (request,id=0):
#     if request.method== 'GET':
#         if id ==0:
#             form = EmployeeForm()
#             return render(request,"employee_register/employee_form.html",{'form':form})
#         else:
#             employee=Employee.objects.get(pk=id)
#             form = EmployeeForm(instance=employee)
#         return render(request,"employee_register/employee_form.html",{'form':form})
#     else:
#         if id==0:
#             form=EmployeeForm(request.POST)
#         else :
#             employee= Employee.objects.get(pk=id)
#             form= EmployeeForm(request.POST,instance=employee)
#         if form.is_valid():
#             form.save()
#         return redirect('/employee/list')

# def employee_delete(request,id):
#     employee = Employee.objects.get(pk=id)
#     employee.delete()
#     return redirect('/employee/list')


