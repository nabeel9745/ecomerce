import email
from django.shortcuts import render,redirect

# Create your views here.

from .models import *

def eg(request):
    if request.method =='POST':
        name=request.POST['name']
        password=request.POST['password']
        email=request.POST['email']
        phn=request.POST['phn']
        address=request.POST['address']
        # x = registration( name=name,password=password,email=email,phn=phn,address=address )
        # x.save()
        registration( name=name,password=password,email=email,phn=phn,address=address ).save()
    return render(request,'common/mvt_eg.html')  

def display(request):
    return render(request,'common/eg2.html')    

def get(request):
    x = int(request.GET['first'])
    y = int(request.GET['second'])
    c=x+y
    print(c)
    return render(request,'common/mvt_get.html',{'c':c})    

def add(request):
    if request.method == 'POST':
        a = int(request.POST['first'])
        b = int(request.POST['second'])
        c = a+b
        return render(request,'common/post_add.html',{'result':c})

    return render(request,'common/post_add.html')  

def retrive(request):
    a = registration.objects.all()
    return render(request,'common/mvt_retrive.html',{'display':a})

def delete(request,id):
    registration.objects.get(id=id).delete()
    return redirect('retrive')

def Update(request,id):
    x = registration.objects.get(id=id)
    return render(request,'common/update_retriveitems.html',{'update_list':x})  

def edit_update(request,id):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        email=request.POST['email']
        phn=request.POST['phn']
        address=request.POST['address']
        registration.objects.filter(id=id).update( name=name,password=password,email=email,phn=phn,address=address)

        return redirect('retrive')

def login(request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']
        try :
            z = registration.objects.get(email = user,password = password)
            request.session['mysession'] = z.id
            return redirect('retrive')
        except registration.DoesNotExist:
             return render(request,'common/loginpg.html',{'message':'wrong input'})
    return render(request,'common/loginpg.html')

def logout(request):
    # request.session.delete('mysession')
    del request.session['mysession']
    return redirect('login')

def user(request):
    # print(request.session['mysession'])
    x = request.session['mysession']
    y = registration.objects.get(id=x)
    return render(request,'common/userdetails.html',{'key':y})
    