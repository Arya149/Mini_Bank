from django.shortcuts import render
from Employee.models import Customer
# Create your views here.
def new_user(request):
    return render(request,'new_user.html')
from .models import New_Customer
def customer_request(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        fname=request.POST.get('fname')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        actype=request.POST.get('account_type')
        
        password=request.POST.get('password')
        a=Customer.objects.filter(Customer_Email=email).count()
        if a==1:
            return render(request,'new_user.html',{'messages':'Email Id is already exists'})
        a=New_Customer.objects.get_or_create(
            Customer_Name=name,
            Customer_Phone=phone,
            Customer_Address=address,
            Customer_Email=email,
            Customer_FName=fname,
            Customer_Password=password,
            Customer_Balance=0.0,
            Customer_Account_Type=actype)
        return render(request,'new_user.html',{'messages':'Request Sent Successfully, We will send the email if your request verifed'})
    else:
        return render(request,'new_user.html')


