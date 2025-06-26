from django.db import models

# Create your models here.
class Employee(models.Model):
    Employee_Id=models.IntegerField()
    Employee_Name=models.CharField(max_length=30)
    Employee_Email=models.EmailField()
    Employee_Password=models.CharField(max_length=10)
    Employee_Mobile=models.CharField(max_length=10)
    Employee_Address=models.TextField()
    Employee_login=models.DateField()