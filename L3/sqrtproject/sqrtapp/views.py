from django.shortcuts import render

def square(request):
    if request.GET.get("num"):
        num = float(request.GET.get("num"))
        res = num ** 0.5
        res = round(res,2)
        msg = "Square root = " + str(res)
        return render(request,"index.html",{"msg":msg})
    else:
        return render(request,"index.html")