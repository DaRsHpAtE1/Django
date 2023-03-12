import requests
try:
    url = 'http://localhost:8000/msg'
    headers = {'Authorization': 'Token 75feaf1eb6d426c6174cbffd72b3e00e10f0fb80'}
    res = requests.get(url, headers=headers)
    print(res)
    data = res.json()
    print(data)
    msg = data['message']
    print(msg)
except Exception as e:
    print('Error:', e)
