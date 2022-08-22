from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request,"index.html")

def add_customer(request):
    return render(request,"add_customer.html")

def customer_table(request):
    return render(request, 'customer_table.html')   

def product(request):
    return render(request, 'product.html')

def add_product(request):
    return render(request, 'add_product.html')

def vendor(request):
    return render(request, 'vendor.html')

def add_vendor(request):
    return render(request, 'add_vendor.html')

def service(request):
    return render(request, 'service.html')

def add_service(request):
    return render(request, 'add_service.html')

def buy_product(request):
    return render(request, 'buy_product.html')

def sell_product(request):
    return render(request, 'sell_product.html')

def sell_services(request):
    return render(request, 'sell_services.html')

def sales_list(request):
    return render(request, 'sales_list.html')