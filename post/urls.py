from django.urls import path
from .views import post

urlpatterns=[
    path('index/',post,name='postIn')
]