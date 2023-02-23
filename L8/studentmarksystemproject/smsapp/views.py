from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentModel

def remove(request,id):
    st = StudentModel.objects.get(rno=id)
    st.delete()
    return redirect('home')

def home(request):
    data = StudentModel.objects.all()
    return render(request,'index.html',{'data':data})

def create(request):
    if request.method == 'POST':
        data = StudentForm(request.POST)
        if data.is_valid():
            data.save()
            msg = 'Record Saved'
            fm  = StudentForm()
            return render(request,'create.html',{'fm':fm,'msg':msg})
        else:
            msg = 'Invalid Data'
            return render(request,'create.html',{'fm':fm,'msg':msg})
    else: 
        fm = StudentForm()
        return render(request,'create.html',{'fm':fm})