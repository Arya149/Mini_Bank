from django.contrib import admin

# Register your models here.
from .models import New_Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=['Customer_Name','Customer_Phone','Customer_Address','Customer_Email','Customer_FName','Customer_Account_Type','Customer_Balance']
admin.site.register(New_Customer,CustomerAdmin)