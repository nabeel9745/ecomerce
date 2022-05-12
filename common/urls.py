from django.urls import path
from .import views

app_name='common'

urlpatterns=[
path('customerregister',views.customerregister),
path('login',views.login),
]