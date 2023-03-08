from django.shortcuts import render

def home(request):
    if request.GET.get("num"):
        try:
            num=int(request.GET.get("num"))
            if num%2==0:
                msg = "Even Number"
            else:
                msg = "Odd Number"
            return render(request,"home.html",{"msg":msg})
        except ValueError:
            msg = 'Enter a valid number'
            return render(request,"home.html",{"msg":msg})
    else:
        return render(request,"home.html")
