from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
# Create your views here.

# def index(request):
#     return render(request,'home_folder/index.html')

class IndexView(TemplateView):
    template_name= 'home_folder/index.html'




