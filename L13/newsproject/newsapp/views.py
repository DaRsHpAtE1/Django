from django.shortcuts import render
from .forms import StudentForm
from .models import StudentModel
from django.core.mail import send_mail

def home(request):
    if request.method == 'POST' and request.POST.get('b1'):
        em = request.POST.get('email')
        try:
            usr = StudentModel.objects.get(email=em)
            fm = StudentForm()
            subject = 'Mail from Django'
            text = 'Hello, this is a mail from Django'
            from_email = ''
            to_email = [str(em)]
            send_mail(subject,text,from_email,to_email)
            return render(request, 'home.html', {'msg':'Email already exists','fm':fm})
        except StudentModel.DoesNotExist:
            data = StudentForm(request.POST)
            data.save()
            fm = StudentForm()
            return render(request, 'home.html', {'msg':'Email registered successfully','fm':fm})
    elif request.method == 'POST' and request.POST.get('b2'):
        em = request.POST.get['email']
        try:
            usr = StudentModel.objects.get(email=em)
            usr.delete()
            fm = StudentForm()
            subject = 'Mail from Django'
            text = 'Hello, this is a mail from Django'
            from_email = ''
            to_email = [str(em)]
            send_mail(subject,text,from_email,to_email)

            return render(request, 'home.html', {'msg':'Email Unregistered','fm':fm})
        except StudentModel.DoesNotExist:
            fm = StudentForm()
            return render(request, 'home.html', {'msg':'Email not registered ','fm':fm})
    else:
        fm = StudentForm()
        return render(request, 'home.html', {'fm':fm})