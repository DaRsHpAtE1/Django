from django.shortcuts import render

def home(request):
    if request.GET.get("num","num"):
        n1=int(request.GET.get("num"))
        n2=int(request.GET.get("num"))
        res=n1+n2
        msg="Addition is "+str((res))
        return render(request,"home.html",{"msg":msg})
    else:
        return render(request,"home.html")