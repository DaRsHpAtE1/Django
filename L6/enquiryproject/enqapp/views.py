from django.shortcuts import render
from .forms import EnForm
from .models import EnModel

# Create your views here.
def enq(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ph = int(request.POST.get('phone'))
        su = request.POST.get('subject')
        data = EnModel(name=na,phone=ph,subject=su)
        data.save()
        msg = "Thank You For The Enquiry"
        fm = EnForm()
        return render(request,'index.html',{'fm':fm,'msg':msg})
    else:
        fm = EnForm()
        return render(request,'index.html',{'fm':fm})