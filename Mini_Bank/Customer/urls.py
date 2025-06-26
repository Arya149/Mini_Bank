

from django.contrib import admin
from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^$',views.clogin, name='clogin'),
    re_path(r'^customer_view$',views.customer_view),
    re_path(r'^transfer_fund$',views.transfer_fund),
    re_path(r'^recent_transactions$',views.recent_transactions),
    re_path(r'^c_forgot_password$',views.c_forgot_password),
    re_path(r'^c_change_password$',views.c_change_password)
  
    ]