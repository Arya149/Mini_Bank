from django.contrib import admin
from django.urls import path,re_path,include
from Manager import views
urlpatterns = [
    re_path(r'^$',views.mlogin),
    re_path(r'^verify_login$',views.verify_login),
    re_path(r'^manage_employees$',views.manage_employees),
    re_path(r'^hire_employee$',views.hire_employee),
    re_path(r'^add_employee$',views.add_employee),
    re_path(r'^employee_view$',views.employee_view),
    re_path(r'^delete_employee$',views.delete_employee),
    re_path(r'^view_transaction$',views.view_transaction),
    re_path(r'^offical_fund_transfer$',views.offical_fund_transfer),
    re_path(r'^customer_management$',views.customer_management),
    re_path(r'^add_customer$',views.add_customer),
    re_path(r'^delete_customer$',views.delete_customer),
    re_path(r'^customer_details$',views.customer_details),
    re_path(r'^view_new_customer_details$',views.view_new_customer_details),
    re_path(r'^new_customer_view$',views.new_customer_view),
    re_path(r'^add_new_customer$',views.add_new_customer),
    re_path(r'^delete_new_customer$',views.delete_new_customer, ),
    re_path(r'^deposit_money$',views.deposit_fund, name='deposit_fund'),
    re_path(r'^withdraw_money$',views.withdraw_fund,name='withdraw_fund')

    ]
