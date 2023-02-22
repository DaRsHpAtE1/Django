from django.shortcuts import render
from .models import FbModel
from .forms import FbForms

def feedback(request):
    if request.method == "POST":
        data = FbForms(request.POST)
        data.save()
        msg = "We have recieved your feedback"
        fm = FbForms()
        return render(request, "index.html", {"fm":fm,"msg":msg})
    else:
        fm = FbForms()
        return render(request, "index.html", {"fm":fm})