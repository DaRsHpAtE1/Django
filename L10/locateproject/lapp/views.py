from django.shortcuts import render
from folium import *

def home(request):
    return render(request,'home.html')

def locate(request):
    loc = [19.1257, 72.8427]
    f = Figure(width=500, height=500)
    andheri = Map(location=loc, zoom_start=18).add_to(f)
    Marker(loc,tool_tip='Navnit CHS').add_to(andheri)
    andheri_html=andheri._repr_html_()
    return render(request,'locate.html',{'msg':andheri_html})