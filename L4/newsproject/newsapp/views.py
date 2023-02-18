from django.shortcuts import render
import requests
# Create your views here.


def news(request):
    if request.GET.get('country'):
        country = request.GET.get('country')
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey=27c6098c9b1e45aca14a1788a572adf7'
        data = requests.get(url).json()
        news = data['articles'][10]
        return render(request, 'index.html', {'news': news})
    return render(request,'index.html')


    
