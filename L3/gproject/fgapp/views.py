from django.shortcuts import render

def grade(request):
    if request.POST.get("marks"):
        marks=int(request.POST.get("marks"))
        if marks > 80:
            grade = "A"
        elif marks > 60:
            grade = "B"
        elif marks > 40:
            grade = "C"
        else:
            grade="D"
        msg="marks = " + str(marks)+ " Grade = "+ grade
        return render(request,"index.html",{"msg":msg})
    else:
        return render(request,"index.html")
        