from django.shortcuts import render

def mult(request):
    if request.POST.get("num1"):
        request.POST.get("num2")
        n1=float(request.POST.get("num1"))
        n2=float(request.POST.get("num2"))
        pro=n1*n2
        msg="Product is "+str((pro))
        return render(request,"index.html",{"msg":msg})
    else:
        return render(request,"index.html")