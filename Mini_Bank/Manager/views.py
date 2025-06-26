from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def service(request):
    return render(request,'service.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def mlogin(request):
    return render(request,'mlogin.html')

def verify_login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        passwrod=request.POST.get('password')
        if email=='arya.iyyappan14@gmail.com' and passwrod=='Arya@2007':
            return render(request,'manager_home.html')
        else:
            return render(request,'mlogin.html',{'messages':'Enter Valid Data'})
    return render(request,'mlogin.html')

def manage_employees(request):
    return render(request,'manager_employees.html')

def hire_employee(request):
    return render(request,'hire_employee.html')
import random
from Manager.models import Employee

def idcreator(request):
    ID=''
    ID+=str(random.randint(1,9))
    for x in range(2):
        ID+=str(random.randint(0,9))
    id=Employee.objects.filter(Employee_Id=ID)
    if id:
        idcreator(request)
    else:
        return ID
import datetime
def add_employee(request):
    if request.method=='POST':
        Name=request.POST.get('name')
        Password=request.POST.get('password')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        email=request.POST.get('email')
        email_check=Employee.objects.filter(Employee_Email=email)
        count=email_check.count()
        if count==1:
            return render(request,'hire_employee.html',{'messages':'Email id is already exist'})
        ID=idcreator(request)
        Employee_login=datetime.datetime.now()
        a=Employee.objects.get_or_create(Employee_Id=ID,Employee_Name=Name,Employee_Email=email,Employee_Address=address,Employee_Password=Password,Employee_Mobile=phone,Employee_login=Employee_login)
        return render(request,'manager_employees.html',{'messages':'Employee Added Successfully '})
    else:
        return render(request,'manager_home.html',{'messages':'Error Occured'})
    
def employee_view(request):
    details=Employee.objects.all()
    return render(request,'view_employee.html',{'details':details})

def delete_employee(request):
    if request.method=='POST':
        Id=request.POST.get('id')
        name=request.POST.get('name')
        email=request.POST.get('email')
        try:
            employee=Employee.objects.get(Employee_Id=Id,Employee_Email=email)
        except Exception as m:
            return render(request,'delete_employee.html',{'messages':m})
       
    
        return render(request,'delete_employee.html',{'messages':'Employee Deleted Successfully!!!'})
    else:
        return render(request,'delete_employee.html')
from Customer.models import Transaction
def view_transaction(request):
    transactions=Transaction.objects.all()
    context = {
        'transactions': transactions,
        'user_role': 'manager'  # Assuming 'role' is 'employee' or 'manager'
    }
    return render(request, 'view_transaction.html', context)
from Employee.models import Customer
def offical_fund_transfer(request):
    if request.method=='POST':
        
        from_account=request.POST.get('from_account')
        customer=Customer.objects.get(Customer_AccountNo=from_account)
        to_account=request.POST.get('to_account')
        amount=int(request.POST.get('amount'))
        remark=request.POST.get('remark')
        try:
            from_c=Customer.objects.get(Customer_AccountNo=from_account)
            send_mail(
                subject='Fund Deposited Successfully',
                message=(
                    f'Dear customer,\n\n₹{amount} has been successfully transfer from your account to {to_account} ({to_c.Customer_Name}).\n'
                    f'New Balance: ₹{int(from_c.Customer_Balance)}\nDate & Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\nBy Employee \n\nThank you.'
                ),
                from_email='arya.iyyappan14@gmail.com',
                recipient_list=[from_c.Customer_Email],
                fail_silently=False,
            )
        except:
            return render(request,'offical_fund_transfer.html',{'messages':'Enter Correct From Account Number','customer':customer})
        try:
            to_c=Customer.objects.get(Customer_AccountNo=to_account)
            send_mail(
                subject='Fund Deposited Successfully',
                message=(
                    f'Dear customer,\n\n₹{amount} has been received from {from_account} account.\n'
                    f'New Balance: ₹{int(int(to_c.Customer_Balance)+int(amount))}\nDate & Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\nBy Employee \n\nThank you.'
                ),
                from_email='arya.iyyappan14@gmail.com',
                recipient_list=[to_c.Customer_Email],
                fail_silently=False,
            )
        except:
            return render(request,'offical_fund_transfer.html',{'messages':'Enter Correct Recipient Account Number','customer':customer})
        balance=Customer.objects.get(Customer_AccountNo=from_account)
        a=[balance.Customer_Balance,amount]

        if int(balance.Customer_Balance) < int(amount):
            return render(request,'offical_fund_transfer.html',{'messages':'Insufficent Balance','customer':customer})
        try:
            from_c=Customer.objects.get(Customer_AccountNo=from_account)
            from_c.Customer_Balance=int(from_c.Customer_Balance)-int(amount)
            from_c.save()
        except Exception as m:
            return render(request,'offical_fund_transfer.html',{'messages': m,'customer':customer})
        try:
            to_c.Customer_Balance=int(to_c.Customer_Balance)+int(amount)
            to_c.save()
        except Exception as m:
            return render(request,'offical_fund_transfer.html',{'messages': m,'customer':customer})
        try:
            if remark=='':
              state=Transaction.objects.get_or_create(From_account=from_account,To_account=to_account,Amount=amount)
              return render(request,'manager_home.html',{'messages':'Fund Trasnfred Successfully','customer':customer})
            else:
              state=Transaction.objects.get_or_create(From_account=from_account,To_account=to_account,Amount=amount,Remarks=remark)
              return render(request,'manager_home.html',{'messages':'Fund Trasnfred Successfully','customer':customer})
        except Exception as m:
             return render(request,'offical_fund_transfer.html',{'messages': m,'customer':customer})     
    else:
        customer=Customer.objects.get(Customer_AccountNo=request.session['account'])
        return render(request,'offical_fund_transfer.html',{'customer':customer})
    
def customer_management(request):
    return render(request,'employee_customer.html')
def accountcreator(request):
    ID=''
    ID+=str(random.randint(1,9))
    for x in range(4):
        ID+=str(random.randint(0,9))
    id=Employee.objects.filter(Employee_Id=ID)
    if id:
        accountcreator(request)
    else:
        return ID
def add_customer(request):
    if request.method=='POST':
        name=request.POST.get('name')
        fname=request.POST.get('fname')
        address=request.POST.get('address')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        balance=request.POST.get('balance')
        type=request.POST.get('account_type')
        a=Customer.objects.filter(Customer_Email=email)
        if a.count()==1:
            return render(request,'add_customer.html',{'messages':'Email Id is already Created By another Customer'})
        accountno=accountcreator(request)
        try:
            a=Customer.objects.get_or_create(Customer_AccountNo=accountno,Customer_Name=name,Customer_Phone=phone,Customer_Address=address,Customer_Email=email,Customer_FName=fname,Customer_Password=password,Customer_Balance=balance,Customer_Account_Type=type)
        except Exception as m:
            return render(request,'add_customer.html',{'messages':m})
        customer_det=Customer.objects.get(Customer_AccountNo=accountno,Customer_Email=email)
        return render(request,'customer_view.html',{'messages':'Account Created Successfully','customer_det':customer_det,'Name':customer_det.Customer_Name})
    else:
        return render(request,'add_customer.html')
    
def delete_customer(request):
    if request.method=='POST':
        account=request.POST.get('account')
        email=request.POST.get('email')
        try:
           obj=Customer.objects.get(Customer_AccountNo=account,Customer_Email=email)
        except Exception as m:
            return render(request,'delete_customer.html',{'messages':m})
        if obj.Customer_Balance==0:
            obj.delete()
            return render(request,'delete_customer.html',{'messages':'Customer Deleted Successfully'})
        else:
            return render(request,'delete_customer.html',{'messages':'Customer Having Money in the Account'})
    else:
        return render(request,'delete_customer.html')
    
def customer_details(request):
    customer=Customer.objects.all()
    return render(request,'customer_details.html',{'customers':customer})
from New_customer.models import New_Customer
def view_new_customer_details(request):
    customer_det=New_Customer.objects.all()
    return render(request,'new_customer_details.html',{'customer_det':customer_det})

def new_customer_view(request):
    if request.method=='POST':
        email=request.POST.get('email')
        customer_det=New_Customer.objects.get(Customer_Email=email)
        return render(request,'new_customer_view.html',{'customer_det':customer_det})
    else:
        return render(request,'new_customer_details.html',{'messages':'Record Not Found','customer_det':customer_det})
   
from django.core.mail import send_mail 

def add_new_customer(request):
    if request.method == 'POST':
        customer_det=New_Customer.objects.all()
        try:
            email=request.POST.get('email')
            customer=New_Customer.objects.get(Customer_Email=email)
        except:
            return render(request,'new_customer_details.html',{'customer_det':customer_det})
        try:
            
            account_no=accountcreator(request)
            customer.delete()
            cust=Customer.objects.get_or_create(
            Customer_AccountNo=account_no,
            Customer_Name=customer.Customer_Name,
            Customer_Phone=customer.Customer_Phone,
            Customer_Email=email,
            Customer_Address=customer.Customer_Address,
            Customer_FName=customer.Customer_FName,
            Customer_Password=customer.Customer_Password,
            Customer_Balance=customer.Customer_Balance,
            Customer_Account_Type=customer.Customer_Account_Type)
            message=f'''
             Your request is accept and your account is created successfully sir,
             Your Account Number is {account_no}, and you can login with this Account Number 
             and Password you given while giving request
                        Thanking You sir    '''
            send_mail(
                    subject='Account Created Successfully',
                    message=message,
                    from_email='arya.iyyappan14@gmail.com',
                    recipient_list=[email],
                    fail_silently=False,
                )
            customer_det=New_Customer.objects.all()
        except Exception as m:
            return render(request,'new_customer_details.html',{'messages':m,'customer_det':customer_det})
        return render(request,'new_customer_details.html',{'messages':'Account Created Successfully','customer_det':customer_det})


def delete_new_customer(request):
    if request.method =='POST':
        customer_det=New_Customer.objects.all()

        try:
            email=request.POST.get('email')
            customer=New_Customer.objects.get(Customer_Email=email)
        except :
             return render(request,'new_customer_details.html',{'customer_det':customer_det})
        if customer:
            customer.delete()
            try:
                send_mail(
                    subject='Account Created Successfully',
                    message="Your Request was Rejected by the employee. Visit our branch in personal to create account",
                    from_email='arya.iyyappan14@gmail.com',
                    recipient_list=[email],
                    fail_silently=False,
                )
                customer_det=New_Customer.objects.all()
            except Exception as m:
                return render(request,'new_customer_details.html',{'messages':m,'customer_det':customer_det}) 

            return render(request,'new_customer_details.html',{'messages':'Account Deleted Successfully','customer_det':customer_det}) 
    else:
        return render(request,'new_customer_details.html',{'customer_det':customer_det})
from decimal import Decimal, InvalidOperation
from django.core.mail import send_mail

from django.shortcuts import render
from Employee.models import Customer
from django.http import HttpResponse
from datetime import datetime
def deposit_fund(request):
    if request.method == 'POST':
        try:
            account_no = request.POST.get('accountno')
            email = request.POST.get('email')
            amount = request.POST.get('amount')

            customer = Customer.objects.get(Customer_AccountNo=account_no)

            # Update balance using Decimal
            original_balance = customer.Customer_Balance
            customer.Customer_Balance =int(int(amount)+int(original_balance))
            balance=int(int(amount)+int(original_balance))
            customer.save()
           
            # Send email
            send_mail(
                subject='Fund Deposited Successfully',
                message=(
                    f'Dear customer,\n\n₹{amount} has been successfully deposited to your account.\n'
                    f'New Balance: ₹{balance}\nDate & Time: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\nThank you.'
                ),
                from_email='arya.iyyappan14@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )

            return render(request, 'manager_home.html', {'messages': 'Fund Deposited Successfully'})

        except Exception as m:
            return render(request, 'deposit_money.html', {'messages': f'Error: {m}'})
    return render(request, 'deposit_money.html')

def withdraw_fund(request):
    if request.method == 'POST':
        try:
            account_no = request.POST.get('accountno')
            email = request.POST.get('email')
            amount = request.POST.get('amount')

            customer = Customer.objects.get(Customer_AccountNo=account_no)

            # Update balance using Decimal
            original_balance = customer.Customer_Balance
            if int(original_balance)<int(amount):
                return render(request, 'withdraw_money.html', {'messages': 'Insufficient Balance'})
            customer.Customer_Balance =int(int(original_balance)-int(amount))
            balance=int(+int(original_balance)-int(amount))
            customer.save()
           
            # Send email
            send_mail(
                subject='Fund Withdrawedd Successfully',
                message=(
                    f'Dear customer,\n\n₹{amount} has been successfully Withdrawed to your account.\n'
                    f'New Balance: ₹{balance}\nDate & Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\nThank you.'
                ),
                from_email='arya.iyyappan14@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )

            return render(request, 'manager_home.html', {'messages': 'Fund Withdrawed Successfully'})

        except Exception as m:
            return render(request, 'withdraw_money.html', {'messages': f'Error: {m}'})
    return render(request, 'withdraw_money.html')
