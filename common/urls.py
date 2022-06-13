from django.urls import path
from .import views

app_name='common'

urlpatterns=[
path('customerregistration',views.customerregister),
path('login',views.login),
path('new',views.new),
]