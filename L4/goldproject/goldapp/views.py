from django.shortcuts import render
import requests

# Create your views here.
def gold(request):
    if requests.GET.get('gold'):
        gold = requests.GET.get("gold")
        gold = gold.upper()
        key='f79bbb9bb7fae1a8f00ec425645ac1b5'
        url = 'https://api.metalpriceapi.com/v1/latest?api_key={key}'
        response = requests.get(url)
        data = response.json()
        rate = data['base'][gold]
        rate = f'Price of {gold} is {rate}'
        return render(request,'index.html',{'rate':rate})
    else:
        return render(request,'index.html')