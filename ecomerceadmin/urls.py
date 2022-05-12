from django.urls import path
from .import views

app_name='ecomerceadmin'

urlpatterns=[
path('home',views.home),
path('viewsellers',views.viewsellers),
]