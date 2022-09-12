from django.urls import path
from .import views


urlpatterns=[
path('ajx_eg',views.ajx_eg,name='ajx_eg'),
path('ajeg',views.ajeg),
path('hello',views.hello,name='hello'),




]