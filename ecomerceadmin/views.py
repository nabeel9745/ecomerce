from django.shortcuts import render

# Create your views here.

def script(request):
    return render(request,'admin/script.html')

def viewsellers(request):
    return render(request,'admin/view sellers.html')    

def dan(request):
    return render(request,'admin/dan.html')  

def logic(request):
        return render(request,'admin/logic.html')

def note(request):
        return render(request,'admin/note.html')    

def eg(request):
    return render(request,'admin/eg.html')

def example(request):
    return render(request,'admin/examples.html')  

def validation(request):
    return render(request,'admin/validation.html')      

def sign(request):
    return render(request,'admin/signupvalidation.html')                 

def s(request):
    return render(request,'admin/script2.html')
