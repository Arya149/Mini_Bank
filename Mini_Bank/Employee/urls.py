from django.contrib import admin
from django.urls import path,re_path,include
from Employee import views
urlpatterns = [
    re_path(r'^$',views.elogin),
    re_path(r'^verify_elogin$',views.verify_elogin),
    re_path(r'^e_forgot_password$',views.e_forgot_password),
    re_path(r'^employee_customer$',views.employee_customer,name='customer_management'),
    re_path(r'^add_customer$',views.add_customer),
    re_path(r'^delete_customer$',views.delete_customer),
    re_path(r'^e_change_password$',views.e_change_password),
    re_path(r'^customer_details$',views.customer_details),
    re_path(r'^view_transactions$',views.view_transactions),
    re_path(r'^offical_fund_transfer$',views.offical_fund_transfer),
    re_path(r'^deposit_money$',views.deposit_fund),
    re_path(r'^withdraw_money$',views.withdraw_fund),


    ]
