from django.shortcuts import render
from .forms import FbForm
from .models import FbModel

# Create your views here.
def fb(request):
    if request.method == "POST":
        na = request.POST.get('name')
        fb= request.POST.get('feedback')
        data = FbModel(name=na,feedback = fb)
        data.save()
        msg = "Thank You For Your Feedback"
        fm = FbForm()
        return render(request,'index.html',{'fm':fm,'msg':msg})
    else:
        fm = FbForm()
        return render(request,'index.html',{'fm':fm})