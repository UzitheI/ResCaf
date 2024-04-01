from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
# Create your views here.

# def index(request):
#     return render(request,'home_folder/index.html')

class IndexView(TemplateView):
    template_name= 'home_folder/index.html'

# def employee_list(request):
#     context = {'employee_list' :Employee.objects.all()}
#     return render(request,"employee_register/employee_list.html",context)

class MenuView(TemplateView):
    template_name='home_folder/menu-1.html'
    

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


