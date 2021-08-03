from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'login/index.html')

def detail (request,question_id):
    return HttpResponse("youre looking at question %s.hhhhh",question_id)