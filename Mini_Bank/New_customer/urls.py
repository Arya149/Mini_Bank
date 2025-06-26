
from django.contrib import admin
from django.urls import path,re_path,include
from . import views
urlpatterns = [
      re_path(r'^$',views.new_user),
      re_path(r'^customer_request$',views.customer_request, name='customer_request'),
]


