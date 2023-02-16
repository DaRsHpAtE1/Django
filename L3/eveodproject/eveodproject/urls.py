
from django.contrib import admin
from django.urls import path
from eoapp.views import eve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',eve)
]
