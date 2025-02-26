from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentModel

def remove(request,id):
    st = StudentModel.objects.get(rno=id)
    st =  ms.delete()
    st.delete()
    return redirect('home')

def home(request):
    data = StudentModel.objects.all()
    return render(request,'index.html',{'data':data})

def create(request):
    if request.method == 'POST':
        data = StudentForm(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            msg = 'Record Saved'
            fm  = StudentForm()
            return render(request,'create.html',{'fm':fm,'msg':msg})
        else:
            msg = 'Invalid Data'
            return render(request,'create.html',{'fm':data,'msg':msg})
    else: 
        fm = StudentForm()
        return render(request,'create.html',{'fm':fm})