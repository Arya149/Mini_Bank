from django.db import models

# Create your models here.

class New_Customer(models.Model):
    Customer_Name=models.CharField(max_length=20)
    Customer_Phone=models.CharField(max_length=10)
    Customer_Address=models.TextField()
    Customer_Email=models.EmailField(primary_key=True)
    Customer_FName=models.CharField(max_length=20)
    Customer_Password=models.CharField(max_length=10)
    Customer_Balance=models.DecimalField(max_digits=9,decimal_places=2 ,null=False)
    Customer_Account_Type=models.CharField(max_length=12)
