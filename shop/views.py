from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def service(request):
    return render(request,'service/index.html')

def blog(request):
    return render(request,'blog/index.html')