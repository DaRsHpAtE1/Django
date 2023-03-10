import requests
while True:
    try:
        inp = int(input('1. Create 2. View 3. Update 4. Delete 5. Exit\n'))
        if inp == 1:
            eid = int(input('Enter Employee ID: '))
            ename = input('Enter Employee Name: ')
            emp = {'eid': eid, 'ename': ename}
            url = 'http://127.0.0.1:8000/empop'
            res = requests.post(url, emp)
            data = res.json()
            print(data)
        elif inp == 2:
            url = 'http://127.0.0.1:8000/empop'
            res = requests.get(url)
            data = res.json()
            print(data)
        elif inp == 3:
            pass
        elif inp == 4:
            eid = int(input('Enter Employee ID: '))
            url = 'http://127.0.0.1:8000/empop' + '/' + str(eid)
            res = requests.get(url)
            if res.status_code == 404:
                print(eid, ' Not Found')
            else:
                data = res.json()
                print(data)
        elif inp == 5:
            break
        else:
            print('Invalid Input')
    except Exception as e:
        print('Issue: ', e)
