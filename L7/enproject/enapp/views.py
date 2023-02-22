from django.shortcuts import render
from .forms import EnForms
from .models import EnModel

def enquiry(request):
    if request.method == "POST":
        data = EnForms(request.POST)
        data.save()
        msg = "We have recieved your response"
        fm = EnForms()
        return render(request, "index.html", {"fm":fm,"msg":msg})
    else:
        fm = EnForms()
        return render(request, "index.html", {"fm":fm})