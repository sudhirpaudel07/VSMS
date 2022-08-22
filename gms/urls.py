"""gms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from .views import customer_table , product, add_product , vendor , add_vendor, service, sales_list, add_service, login , index, add_customer, buy_product, sell_product, sell_services


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login, name="login"),
    path('', index, name="index"),
    path('add_customer',add_customer,name='add_customer'),
    path('customer_table',customer_table,name='customer_table'),
    path('product',product,name='product'),
    path('add_product',add_product,name='add_product'),
    path('vendor',vendor,name='vendor'),
    path('add_vendor',add_vendor,name='add_vendor'),
    path('service',service,name='service'),
    path('add_service',add_service,name='add_service'),
    path('buy_product',buy_product,name='buy_product'),
    path('sell_product',sell_product,name='sell_product'),
    path('sell_services',sell_services,name='sell_services'),
    path('sales_list',sales_list,name='sales_list'),
    

    
]
