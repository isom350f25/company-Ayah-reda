from . import views 
from django.urls import path 

urlpatterns = [
    path('list_employee/', views.employee_list)  
]