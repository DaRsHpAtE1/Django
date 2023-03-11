import requests
from getpass import *
try:
    url = 'http://localhost:8000/msg'
    username = input('Enter username: ')
    password = getpass('Enter password: ')
    res = requests.get(url, auth=(username, password))
    print(res)
    data = res.json()
    print(data)
    msg = data['message']
    print(msg)
except Exception as e:
    print('Error:', e)
