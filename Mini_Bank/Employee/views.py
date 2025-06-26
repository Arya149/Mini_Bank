from django.shortcuts import render
from Manager.models import Employee
from django.http import HttpResponse
import datetime
# Create your views here.
def elogin(request):
    return render(request,'elogin.html')
import datetime
from django.shortcuts import render
from Manager.models import Employee

def verify_elogin(request):
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            a = Employee.objects.filter(Employee_Id=id, Employee_Email=email, Employee_Password=password)
        except Exception as m:
            return render(request, 'elogin.html', {'messages': m})

        if a.count() == 1:
            a = a.first()
            name = a.Employee_Name
            a.Employee_login = datetime.datetime.now()
            a.save()
            return render(request, 'employee_home.html', {
                'messages': 'Logined Successfully',
                'Name': name,
                'Id': id
            })
        else:
            # This was missing: handle login failure!
            return render(request, 'elogin.html', {
                'messages': 'Invalid ID, Email or Password. Please try again.'
            })

    # GET request fallback
    return render(request, 'elogin.html')

from django.core.mail import send_mail
from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string
otp_store={}
from django.core.mail import send_mail
from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string

otp_store = {}

def e_forgot_password(request):
    context = {}
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'send_otp':
            email = request.POST.get('email')
            try:
                validate_email(email)
            except ValidationError:
                context['messages'] = "Invalid email format."
                return render(request, 'e_forgot_password.html', context)

            otp = get_random_string(length=6, allowed_chars='0123456789')
            otp_store[email] = otp

            send_mail(
                subject='Your OTP Code',
                message=f'Your OTP is: {otp}',
                from_email='arya.iyyappan14@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )
            request.session['email']=email
            context['messages'] = "OTP sent to your email."
            context['email'] = email
            context['show_verify'] = True

        elif action == 'verify_otp':
            email = request.POST.get('email')
            otp = request.POST.get('otp')

            if otp_store.get(email) == otp:
                otp_store.pop(email)
                context['messages'] = "OTP verified successfully!"
                return render(request, 'e_change_password.html', context)
            else:
                context['messages'] = "Invalid OTP."
                context['email'] = email
                context['show_verify'] = True

        elif action == 'resend_otp':
            email = request.POST.get('email')
            if email:
                otp = get_random_string(length=6, allowed_chars='0123456789')
                otp_store[email] = otp
                send_mail(
                    subject='Your OTP Code (Resent)',
                    message=f'Your new OTP is: {otp}',
                    from_email='arya.iyyappan14@gmail.com',
                    recipient_list=[email],
                    fail_silently=False,
                )
                context['messages'] = "OTP resent to your email."
                context['email'] = email
                context['show_verify'] = True
            
    return render(request, 'e_forgot_password.html', context)
def e_change_password(request):
    if request.method=='POST':
        if request.POST.get('action')=='change_password':
            password=request.POST.get('new_password1')
            id=Employee.objects.get(Employee_Email=request.session['email'])
            id.Employee_Password=password
            id.save()
            return render(request,'elogin.html',{'messages': 'Password Changed Successfully'})
    else:
        return render(request,'e_forgot_password.html',{'messages':'Error Occured'})


def employee_customer(request):
    return render(request,'employee_customer.html')
import random
from .models import Customer
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
        return render(request,'customer_view.html',{'customer_det':customer_det,'Name':customer_det.Customer_Name})
    else:
        return render(request,'add_customer.html')
    
def delete_customer(request):
    if request.method=='POST':
        account=request.POST.get('account')
        email=request.POST.get('email')
        obj=Customer.objects.get(Customer_AccountNo=account,Customer_Email=email)
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
from Customer.models import Transaction
def view_transactions(request):
    transactions=Transaction.objects.all()
    context = {
        'transactions': transactions,
        'user_role': 'Employee'  # Assuming 'role' is 'employee' or 'manager'
    }
    return render(request, 'view_transaction.html', context)

def offical_fund_transfer(request):
    if request.method=='POST':
        try:
            from_account=request.POST.get('from_account')
            customer=Customer.objects.get(Customer_AccountNo=from_account)
            to_account=request.POST.get('to_account')
            amount=float(request.POST.get('amount'))
            remark=request.POST.get('remark')
        except Exception as m:
                        return render(request,'offical_fund_transfer.html',{'messages':m})

        try:
            from_c=Customer.objects.get(Customer_AccountNo=from_account)
            to_c=Customer.objects.get(Customer_AccountNo=to_account)
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

        if float(balance.Customer_Balance) < float(amount):
            return render(request,'offical_fund_transfer.html',{'messages':'Insufficent Balance','customer':customer})
        try:
            from_c=Customer.objects.get(Customer_AccountNo=from_account)
            from_c.Customer_Balance=float(from_c.Customer_Balance)-float(amount)
            from_c.save()
        except Exception as m:
            return render(request,'offical_fund_transfer.html',{'messages': m,'customer':customer})
        try:
            to_c.Customer_Balance=float(to_c.Customer_Balance)+float(amount)
            to_c.save()
        except Exception as m:
            return render(request,'offical_fund_transfer.html',{'messages': m,'customer':customer})
        try:
            if remark=='':
              state=Transaction.objects.get_or_create(From_account=from_account,To_account=to_account,Amount=amount)
              return render(request,'employee_home.html',{'messages':'Fund Trasnfred Successfully','customer':customer})
            else:
              state=Transaction.objects.get_or_create(From_account=from_account,To_account=to_account,Amount=amount,Remarks=remark)
              return render(request,'employee_home.html',{'messages':'Fund Trasnfred Successfully','customer':customer})
        except Exception as m:
             return render(request,'offical_fund_transfer.html',{'messages': m,'customer':customer})     
    else:
        customer=Customer.objects.get(Customer_AccountNo=request.session['account'])
        return render(request,'offical_fund_transfer.html',{'customer':customer})
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
                    f'New Balance: ₹{balance}\nDate & Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\nBy Employee \n\nThank you.'
                ),
                from_email='arya.iyyappan14@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )

            return render(request, 'employee_home.html', {'messages': 'Fund Deposited Successfully'})

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
                    f'New Balance: ₹{balance}\nDate & Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n By Employee \n\nThank you. '
                ),
                from_email='arya.iyyappan14@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )

            return render(request, 'employee_home.html', {'messages': 'Fund Withdrawed Successfully'})

        except Exception as m:
            return render(request, 'withdraw_money.html', {'messages': f'Error: {m}'})
    return render(request, 'withdraw_money.html')
