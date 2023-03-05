from django.shortcuts import render

def sqrt(request):
    if request.GET.get("num"):
        num=float(request.GET.get("num"))
        res=num*num 
        msg="square = "+ str(round(res,2))
        return render(request,"index.html",{"msg":msg})
    else:
        return render(request,"index.html")
