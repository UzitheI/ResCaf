from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, FormView,View, ListView
from . models import Dish
from .forms import DishForm,searchForm
from django.urls import reverse_lazy

class AddDish(CreateView):
    model=Dish
    form_class=DishForm
    template_name='home_folder/alldish.html'
    success_url=reverse_lazy('createDish')

class SearchListView(ListView):
    model = Dish
    template_name = 'home_folder/alldish.html'
    paginate_by = 10 

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            return self.model.objects.filter(name__icontains=query)
        else:
            return self.model.objects.all()
