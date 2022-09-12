from django.urls import path
from .import views

# app_name='seller'

urlpatterns=[
path('details',views.details,name='details'),
path('show_d',views.show_d,name='show_d'),
path('u_window/<int:id>',views.u_window,name='u_window'),
path('edit_window/<int:id>',views.edit_window,name='edit_window'),
path('login',views.login,name='login'),
path('logout',views.logout,name='logout')
]