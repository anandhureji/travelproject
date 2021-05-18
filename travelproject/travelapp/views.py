from django.http import HttpResponse
from django.shortcuts import render
from .models import place

# Create your views here.
def regform(request):
    return render(request,"Regform.html")

def demo(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})

def about(request):
    name="india"
    return render(request,"about.html",{'obj':name})

def addition(request):
    n1=int(request.GET['num1'])
    n2=int(request.GET['num2'])
    res=n1+n2
    return render(request,"result.html",{'result':res})
