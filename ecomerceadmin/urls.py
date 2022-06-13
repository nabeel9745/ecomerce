from django.urls import path
from .import views

app_name='ecomerceadmin'

urlpatterns=[
path('script',views.script),
path('viewsellers',views.viewsellers),
path('dan',views.dan),
path('logic',views.logic),
path('note',views.note),
path("eg",views.eg),
path("example",views.example),
path('validation',views.validation),
path("sign",views.sign),
]