from django.shortcuts import render
from .models import Blogl
from django.http import HttpResponse
# Create your views here.

def index(request):
    blog=Blogl.objects.all()
    context={'blog':blog}
    return render(request,'blog/index.html',context)