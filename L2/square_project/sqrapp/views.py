from django.shortcuts import render

def home(request):
    if request.GET.get("num"):
        num=float(request.GET.get("num"))
        res=num*num 
        msg="square = "+ str(round(res,2))
        return render(request,"home.html",{"msg":msg})
    else:
        return render(request,"home.html")
