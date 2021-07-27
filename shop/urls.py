from django.urls import path
from .views import index,service,blog

urlpatterns = [
    path('',index,name='index'),
    path('index/',index,name='shopIn'),
    path('home/',index,name='shopHo'),
    path('service/',service, name='serviceMe'),
    path('blog/',blog, name='blogMe'),
]