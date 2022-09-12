from django.urls import path
from .import views

# app_name='common'

urlpatterns=[
path('eg',views.eg),
path('get',views.get, name="get"),
path('display',views.display),
path('add',views.add),
path('retrive',views.retrive, name="retrive"),
path('delete/<int:id>',views.delete,name="delete"),
path('Update/<int:id>',views.Update,name="Update"),
path('edit_update/<int:id>',views.edit_update,name="edit_update"),
path('login',views.login,name="login"),
path('logout',views.logout,name="logout"),
path('user',views.user,name="user"),








]