from django.urls import path
from .import views

app_name='customers'

urlpatterns=[
path('home',views.home),
path('sample',views.sample),
path('p',views.p),
path('todo',views.todo),
path('selectionbox',views.selectionbox),
path('sort',views.sort),
path('jquery',views.jquery),
path('w',views.w),
path('queryhtml',views.queryhtml),
path('todobox',views.todobox),





]