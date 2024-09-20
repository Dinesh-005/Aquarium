from django.shortcuts import render
from django.http import HttpResponse
from .models import data

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def products(request):
    return render(request,'products.html')
def contact(request):
    return render(request,'contact.html')

def contactf(request):
    if request.method=="POST":
        name1=request.POST["name"]
        email1=request.POST["email"]
        number1=request.POST["number"]
        message1=request.POST["message"]

        context={

            'user':name1,
            'mail':email1,
            'no':number1,
            'mes':message1,
        }


        obj=data()
        obj.name=name1,
        obj.email=email1,
        obj.number=number1,
        obj.message=message1,
        obj.save()

        return render(request,'home.html',context)

        
        


