from django.shortcuts import render
from .models import Blogl
from django.http import HttpResponse
# Create your views here.

def index(request):
    blog=Blogl.objects.all()
    context={'blog':blog}
    return render(request,'blog/index.html',context)

def post(request,id):
    obj=Blogl.objects.get(id=id)
    counst={'post':obj}
    return render(request,'blog/post.html',counst)