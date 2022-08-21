from django.shortcuts import render


def abc(request):
    return render(request,"index.html")


def base(request):
    return render(request,"base.html")

def form(request):
    return render(request,"formss.html")

