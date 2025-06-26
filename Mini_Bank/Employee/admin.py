from django.contrib import admin

# Register your models here.
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=['Customer_Name','Customer_Email','Customer_Balance','Customer_AccountNo','Customer_Password']
admin.site.register(Customer,CustomerAdmin)