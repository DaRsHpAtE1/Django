from django.shortcuts import render
import requests
# Create your views here.


def crypto(request):
    try:
        if request.GET.get('crypto'):
            crypto = request.GET.get('crypto')
            crypto = crypto.upper()
            access_key = '27c6098c9b1e45aca14a1788a572adf7'
            url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={access_key}'
            response = requests.get(url)
            data = response.json()
            price = data['rates'][crypto]
            price = f'Price of {crypto} is {price}'
            return render(request, 'index.html', {'price': price})
        else:
            return render(request, 'index.html')
    except Exception as e:
        price = 'Please enter a valid crypto currency'
        return render(request, 'index.html', {'price':price})