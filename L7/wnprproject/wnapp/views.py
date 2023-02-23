from django.shortcuts import render
from .forms import WnForm
from .models import WnModel

# Create your views here.
def index(request):
    if request.method == "POST":
        data = WnForm(request.POST)
        data.save()
        msg = "Great! Your data has been saved."
        fm = WnForm()
        return render(request,'index.html',{'fm':fm,'msg':msg})
    else:
        fm = WnForm()
        return render(request,'index.html',{'fm':fm})