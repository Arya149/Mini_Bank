from django.contrib import admin
from Manager.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['Employee_Id','Employee_Name','Employee_Password','Employee_Mobile','Employee_Address']
admin.site.register(Employee,EmployeeAdmin)