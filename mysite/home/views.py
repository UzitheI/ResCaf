
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from . models import BookATable, ChefDetails, BlogDetails
from .forms import BookingForm
from django.urls import reverse_lazy
from menu.models import Dish
    


class IndexView(ListView):
    template_name='home_folder/index.html'

    def get_queryset(self):
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dishes']= Dish.objects.all()
        context["chefs"] = ChefDetails.objects.all()
        context["blogs"]= BlogDetails.objects.all()
        return context

class BookingView(CreateView):
    model= BookATable
    form_class= BookingForm
    template_name="home_folder/index.html"
    success_url=reverse_lazy('table')
#     context = {'employee_list' :Employee.~objects.all()}
#     return render(request,"employee_register/employee_list.html",context)

class ReservationView(TemplateView):
    template_name= 'home_folder/reservation.html'

class TableUpdatView(UpdateView):
    model=BookATable
    form_class=BookingForm
    template_name="home_folder/index.html"
    success_url=reverse_lazy('tablelist')



