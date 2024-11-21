from django.shortcuts import render,redirect
from .models import studentdata


def home(request):
    sd = studentdata.objects.all()
    return render(request, 'crudapp/home.html', {'sd': sd})


def add_student(request):
    if request.method == 'GET':

        return render(request, 'crudapp/add_student_form.html')
    else:
        studentdata(
            fname=request.POST.get('fname'),
            lname=request.POST.get('lname'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            marks1=request.POST.get('marks1'),
            marks2=request.POST.get('marks2'),
            marks3=request.POST.get('marks3'),
            marks4=request.POST.get('marks4'),
            marks5=request.POST.get('marks5')

        ).save()
        sd = studentdata.objects.all()
        return render(request, 'crudapp/home.html', {'sd': sd})


def update_data(request, id):
    sd = studentdata.objects.get(id=id)
    return render(request, 'crudapp/update_data_form.html', {'sd': sd})


def save_upadte_data(requet, id):
    sd = studentdata.objects.get(id=id)
    sd.fname = requet.POST.get('fname')
    sd.lname = requet.POST.get('lname')
    sd.email = requet.POST.get('email')
    sd.mobile = requet.POST.get('mobile')
    sd.marks1 = requet.POST.get('marks1')
    sd.marks2 = requet.POST.get('marks2')
    sd.marks3 = requet.POST.get('marks3')
    sd.marks4 = requet.POST.get('marks4')
    sd.marks5 = requet.POST.get('marks5')
    sd.save()
    return redirect(home)
    # Create your views here.


def delete_data(request, id):
    sd = studentdata.objects.get(id=id)
    sd.delete()
    return redirect(home)