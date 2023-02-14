from django.shortcuts import render

# Create your views here.


def home(request):
    if request.POST.get('radius'):
        radius = float(request.POST.get('radius'))
        area = 3.14 * radius * radius
        circumference = 2 * 3.14 * radius
        msg = f'Area: {round(area,2)} and Circumference: {round(circumference,2)}'
        return render(request, 'home.html', {'msg': msg})
    else:
        return render(request,'home.html')