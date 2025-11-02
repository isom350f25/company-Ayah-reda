from django.shortcuts import render
from .models import Employee


# Create your views here.
def employee_list(request):
  employees = Employee.objects.all().order_by('name')
  context = {
    'employees': employees, 
  }
  return render(request, "employee_list.html", context)
