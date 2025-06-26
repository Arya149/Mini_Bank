from django.db import models

# Create your models here.
class Customer(models.Model):
    Customer_AccountNo=models.IntegerField(primary_key=True)
    Customer_Name=models.CharField(max_length=20)
    Customer_Phone=models.CharField(max_length=10)
    Customer_Address=models.TextField()
    Customer_Email=models.EmailField(unique=True)
    Customer_FName=models.CharField(max_length=20)
    Customer_Password=models.CharField(max_length=10)
    Customer_Balance=models.IntegerField(null=False)
    Customer_Account_Type=models.CharField(max_length=12)
