from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
  list_display =("name", "position", "joined_on", "phone_number" ,"date_of_birth" )
  search_fields = ('name', 'position')
  list_filter = ('joined_on',)
  pass


