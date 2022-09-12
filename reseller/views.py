from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import*

# Create your views here.

def ajx_eg(request):
    return render(request,'reseller/ajax_method.html')
@csrf_exempt
def ajeg(request):
    a = request.POST['x']
    b = request.POST['y']
    ajax_image(name=a,email=b).save()
    return JsonResponse({'message':'value'})

def hello(request):
    pass
    #  a = students.objects.all()
    # return render(request,'reseller/hllo.html',{'display':a})
