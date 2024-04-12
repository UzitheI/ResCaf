from django.db.models.query import QuerySet
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView,  ListView, TemplateView, UpdateView, DeleteView
from . models import Dish
from .forms import DishForm,searchForm
from django.urls import reverse_lazy

class AddDish(CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'home_folder/alldish.html'
    success_url = reverse_lazy('createDish')

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
    success_url= reverse_lazy('createDish')

class DeleteDish(DeleteView):
    model=Dish
    template_name="home_folder/delete.html"
    success_url=reverse_lazy('createDish')

class MenuView(ListView):
    model= Dish
    template_name='home_folder/menu-1.html'

    def get_context_data(self, **kwargs):
        context= super(). get_context_data(**kwargs)
        context['dishes']=self.get_queryset()
        return context  

# class SearchListView(ListView):
#     model = Dish
#     template_name = 'home_folder/alldish.html'

#     def get_queryset(self):
#         query=self.request.GET.get('q')
#         if query:
#             return self.model.objects.filter(name__icontains=query)

#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         context['query']=self.request.GET.get('q','')
#         context['dishes']=self.object_list
#         return context



# def menu_list_view(request):
#     all_dishes=Dish.objects.all()

#     context={
#         'all_dishes':all_dishes
#     }
#     return render(request, 'menu-1.html',context)

# def fetch_dishes(request, category):
#     if category== 'all':
#         dishes=Dish.objects.all()
    
#     else:
#         dishes=Dish.objects.filter(category=category)
#     return JsonResponse({'dishes':dishes})
