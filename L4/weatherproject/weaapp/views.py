from django.shortcuts import render

# Create your views here.
import requests


def weather(request):
    try:
        if request.POST.get('city'):
            city = request.POST.get('city')
            api_key = "963fa95d5ba0ba96b491b922dcec5b92"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            temperature = data['main']['temp']
            temperature = f'Temperature of {city} is {temperature}'
            return render(request, 'index.html', {'temperature': temperature})
        else:
            return render(request, 'index.html')
    except Exception as e:
        temperature = f'City not found'
        return render(request, 'index.html', {'temperature':temperature})