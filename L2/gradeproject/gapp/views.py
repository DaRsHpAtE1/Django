from django.shortcuts import render

# Create your views here.
def grade(request):
    if request.POST.get("marks"):
        marks=int(request.POST.get("marks"))
        if marks > 80:
            grade = "Student Has Obtained Grade A"
        elif marks > 60:
            grade = "Student Has Obtained Grade B"
        elif marks > 40:
            grade = "Student Has Obtained Grade C"
        else:
            grade="Student Has Obtained Grade D"
        return render(request,"index.html",{"grade":grade})
    else:
        return render(request,"index.html")