from django.shortcuts import render

# Create your views here.

def home(request):
     return render(request,'customer/home.html')

def sample(request):
     return render(request,'customer/sample.html')

def p(request):
     return render(request,'customer/p.html')

def todo(request):
     return render(request,'customer/todo.html')

def selectionbox(request):
     return render(request,'customer/selectionbox.html')

def sort(request):
     return render(request,'customer/sort.html')

def jquery(request):
     return render(request,'customer/jquery.html')

def w(request):
     return render(request,'customer/w.html')

def queryhtml(request):
     return render(request,'customer/queryhtml.html')

def todobox(request):
     return render(request,'customer/todobox.html')
