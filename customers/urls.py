from django.urls import path
from .import views

app_name='customers'

urlpatterns=[
path('home',views.home),
path('sample',views.sample),
]