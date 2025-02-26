"""cmsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from cmsapp.views import home,dept,adddept,remdept,stu,addstu,remstu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('dept',dept,name='dept'),
    path('adddept',adddept,name='adddept'),
    path('remmdept<int:id>',remdept,name='remdept'),
    path('stu',stu,name='stu'),
    path('addstu',addstu,name='addstu'),
    path('remstu<int:id>',remstu,name='remstu'),
]
