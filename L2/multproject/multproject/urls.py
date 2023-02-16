
from django.contrib import admin
from django.urls import path
from mapp.views import mult

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mult)
]
