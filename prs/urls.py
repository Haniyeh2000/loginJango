"""prs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('shop.urls','shopIn'),namespace='shopIn')),
    path('shop/',include(('shop.urls','ushop'),namespace='ushop')),
    path('blog/',include(('blog.urls','blogIn'),namespace='blogIn')),
    path('post/',include(('post.urls','postIn'),namespace='postIn')),
    path('service/',include(('service.urls','serviceIn'),namespace='serviceIn')),
    path('login/',include(('login.urls','loginIn'),namespace='loginIn'))
]
