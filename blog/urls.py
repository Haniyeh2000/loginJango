from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='BlogIndex'),
    path('post/<id>/',views.post,name='BlogPost'),
]