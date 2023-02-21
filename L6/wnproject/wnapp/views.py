from django.shortcuts import render


from django.shortcuts import render
from .forms import WnForm
from .models import WnModel

# Create your views here.
def home(request):
    if request.method == "POST":
        na = request.POST.get('name')
        op= request.POST.get('options')
        data = WnModel(name=na, options = op)
        data.save()
        msg = "Thank You"
        fm = WnForm()
        return render(request,'index.html',{'fm':fm,'msg':msg})
    else:
        fm = WnForm()
        return render(request,'index.html',{'fm':fm})