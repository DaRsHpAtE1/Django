from django.shortcuts import render,redirect

def pnf(request,exception):
    return redirect('home')

def result(request):
    return render(request,'result.html')

def home(request):
    if request.GET.get('num'):
        try:
            num = float(request.GET.get('num'))
            if num >= 0.0:
                res = num ** 0.5
                msg = 'square root = ' + str(round(res,2))
                return render(request,'result.html',{'msg':msg})
            else:
                msg = 'Enter Valid Number which is not negative'
                return render(request,'result.html',{'msg':msg})
        except ValueError:
            msg = 'Enter Valid Number'
            return render(request,'result.html',{'msg':msg})
    else:
        return render(request,'index.html')

