import requests
while True:
    try:
        inp = int(input('Enter 1 for Insert, 2 for Display, 3 for Exit: '))
        if inp == 1:
            rno = int(input('Enter Roll No: '))
            name = input('Enter Name: ')
            stu = {'rno': rno, 'name': name}
            url = 'http://127.0.0.1:8000/stuop'
            res = requests.post(url, stu)
            data = res.json()
            print(data)
        elif inp == 2:
            url = 'http://127.0.0.1:8000/stuop'
            res = requests.get(url)
            data = res.json()
            print(data)
        elif inp == 3:
            break
        else:
            print('Invalid Choice')
    except Exception as e:
        print(e)
