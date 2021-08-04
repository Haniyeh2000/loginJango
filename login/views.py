from django.shortcuts import render
from django.http import HttpResponse
from .models import Login

# Create your views here.
def login(request):
    users = Login.objects.all()
    return render(request,'login/index.html', {'users': users})

def detail (request,question_id):
    return HttpResponse("youre looking at question %s hhhhh" % question_id)