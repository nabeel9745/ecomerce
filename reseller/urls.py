from django.urls import path
from .import views

app_name='reseller'

urlpatterns=[
path('addproject',views.addproject),
path('home',views.home),
]