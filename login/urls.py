from django.urls import path
from .views import login,detail

urlpatterns=[
    path("index/",login,name="loginIn"),
    path('<int:question_id>/',detail,name='loginTest'),
]

