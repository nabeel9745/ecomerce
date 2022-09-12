from django.shortcuts import render,redirect

from seller.models import students

from .models import *

# Create your views here.

def details(request):
    if request.method == 'POST':
        name=request.POST['name']
        cls=request.POST['cls']
        roll=request.POST['roll']
        students(name=name,cls=cls,roll=roll).save()
    return render(request,'seller/details.html')

def show_d(request):
    a = students.objects.all()
    return render(request,'seller/show_details.html',{'display':a})

def u_window(request,id):
    x = students.objects.get(id=id)
    return render(request,'seller/u_window.html',{'updated':x})

def edit_window(request,id):
    if request.method == 'POST':
        name=request.POST['name']
        cls=request.POST['cls']
        roll=request.POST['roll']
        students.objects.filter(id=id).update( name=name,cls=cls,roll=roll)
        return redirect('show_d')

def login(request):
    if request.method == 'POST':
        name=request.POST['name']
        cls=request.POST['cls']
        try:
            x=students.objects.get(name=name,cls=cls)
            request.session['s_session'] = x.id
            return redirect ('show_d')
        except students.DoesNotExist:
            return render(request,'seller/student_login.html',{'msg':'invalid login'})
    return render(request,'seller/student_login.html')

def logout(request):
    del request.session['s_session']
    return redirect('login')
       
