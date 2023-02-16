from django.shortcuts import render

def eve(request):
    if(request.POST.get("num")):
        num = int(request.POST.get("num"))
        if num % 2 ==0:
            res = "Even Number"
        else:
            res = "Odd Number"
        msg = "Result is " +res
        return render(request,"index.html",{"msg":msg})
    else:
        return render(request,"index.html")
