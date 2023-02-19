from django.shortcuts import render
import requests

# Create your views here.
def gold(request):
    if request.GET.get('gold'):
        gold = request.GET.get("gold")
        gold = gold.upper()
        url = 'https://metals-api.com/api/latest?access_key=cso6kd4dpua9357b49cj28dq91j4gojja4o8c3ccf96i9wzdalyza4a8vuw6'
        response = requests.get(url)
        data = response.json()
        rate = data['INR'][gold]
        rate = f'Price of {gold} is {rate}'
        return render(request,'index.html',{'rate':rate})
    else:
        return render(request,'index.html')