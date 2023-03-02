from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def uhome(request):
    if request.user.is_authenticated:
        return redirect('uwelcome')
    else:
        if request.method == 'POST':
            un = request.POST['uname']
            pw = request.POST['upass']
            usr = authenticate(username=uname,password=upass)
            if usr is None:
                return render(request,'uhome.html',{'msg':'Invalid Credentials'})
            else:
                login(request,usr)
                return redirect('uwelcome')
        else:
            return render(request,'uhome.html')

def usignup(request):
    if request.user.is_authenticated:
        return redirect('uwelcome')
    else:
        if request.method == 'POST':
            un = request.POST['uname']
            try:
                User.objects.get(username=un)
                return render(request,'usignup.html',{'msg':'Username already exists'})
            except User.DoesNotExist:
                usr = User.objects.create_user(username=un,password='1234')
                usr.save()
                return redirect('uhome')
        else:
            return render(request,'usignup.html')
        
def uwelcome(request):
    if request.user.is_authenticated:
        return render(request,'uwelcome.html')
    else:
        return redirect('uhome')
    
def ulogout(request):
    logout(request)
    return redirect('uhome')
    