from django.urls import path
from .views import login

urlpatterns=[
    path("index/",login,name="loginIn"),
    path('<int:question_id>/')
]

