"""
URL configuration for Mini_Bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from Manager import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.home,name='home'),
    re_path(r'^service$',views.service,name='service'),
    re_path(r'^about$',views.about,name='about'),
    re_path(r'^contact$',views.contact,name='contact'),
    re_path(r'^manager/',include('Manager.urls')),
    re_path(r'^employee/',include('Employee.urls')),
    re_path(r'^customer/',include('Customer.urls')),
    re_path(r'^new_user/',include('New_customer.urls'))
]
