from django.shortcuts import render
from Employee.models import Customer
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def clogin(request):
    if request.method=='POST':
        account=request.POST.get('accountno')
        email=request.POST.get('email')
        password=request.POST.get('password')
        request.session['account']=account
        try:
            customer=Customer.objects.get(Customer_AccountNo=account,Customer_Email=email,Customer_Password=password)
        except:
            return render(request,'customer_login.html',{'messages':'Enter Valid Data'})
        return render(request,'customer_home.html',{'customer':customer})
    else:
        return render(request,'customer_login.html')
    
def customer_view(request):
    customer_det=Customer.objects.get(Customer_AccountNo=request.session['account'])
    return render(request,'customer_view.html',{'customer_det'
    '':customer_det})
from .models import Transaction
from django.core.mail import send_mail
from datetime import datetime
def transfer_fund(request):
    if request.method=='POST':
        customer=Customer.objects.get(Customer_AccountNo=request.session['account'])
        from_account=request.POST.get('from_account')
        to_account=request.POST.get('to_account')
        amount=float(request.POST.get('amount'))
        remark=request.POST.get('remark')
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
            return render(request,'transfer_fund.html',{'messages':'Enter Correct Recipient Account Number','customer':customer})
        balance=Customer.objects.get(Customer_AccountNo=from_account)
        a=[balance.Customer_Balance,amount]

        if float(balance.Customer_Balance) < float(amount):
            return render(request,'transfer_fund.html',{'messages':'Insufficent Balance','customer':customer})
        try:
            from_c=Customer.objects.get(Customer_AccountNo=from_account)
            from_c.Customer_Balance=float(from_c.Customer_Balance)-float(amount)
            from_c.save()
        except Exception as m:
            return render(request,'transfer_fund.html',{'messages': m,'customer':customer})
        try:
            to_c.Customer_Balance=float(to_c.Customer_Balance)+float(amount)
            to_c.save()
        except Exception as m:
            return render(request,'transfer_fund.html',{'messages': m,'customer':customer})
        try:
            if remark=='':
              state=Transaction.objects.get_or_create(From_account=from_account,To_account=to_account,Amount=amount)
              return render(request,'transfer_fund.html',{'messages':'Fund Trasnfred Successfully','customer':customer})
            else:
              state=Transaction.objects.get_or_create(From_account=from_account,To_account=to_account,Amount=amount,Remarks=remark)
              return render(request,'transfer_fund.html',{'messages':'Fund Trasnfred Successfully','customer':customer})
        except Exception as m:
             return render(request,'transfer_fund.html',{'messages': m,'customer':customer})     
    else:
        customer=Customer.objects.get(Customer_AccountNo=request.session['account'])
        return render(request,'transfer_fund.html',{'customer':customer})
    
def recent_transactions(request):
    obj=Customer.objects.filter
    acc_no=request.session['account']
    transactions = Transaction.objects.filter( Q(From_account=acc_no) | Q(To_account=acc_no)).order_by('-Timestamp')[:10]
    return render(request,'recent_transactions.html',{'transactions':transactions,'acc_no':acc_no})

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

def c_forgot_password(request):
    context = {}
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'send_otp':
            email = request.POST.get('email')
            try:
                validate_email(email)
            except ValidationError:
                context['messages'] = "Invalid email format."
                return render(request, 'c_forgot_password.html', context)

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
                return render(request, 'c_change_password.html', context)
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
            
    return render(request, 'c_forgot_password.html', context)


def c_change_password(request):
    if request.method=='POST':
        if request.POST.get('action')=='change_password':
            password=request.POST.get('new_password1')
            id=Customer.objects.get(Customer_Email=request.session['email'])
            id.Customer_Password=password
            id.save()
            return render(request,'customer_login.html',{'messages': 'Password Changed Successfully'})
    else:
        return render(request,'c_forgot_password.html',{'messages':'Error Occured'})
