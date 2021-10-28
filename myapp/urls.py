
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('index.html',views.home,name='home'),
    path('rafting.html',views.rafting,name='rafting'),
    path('quad.html',views.quad,name='quad'),
    path('pansion.html',views.pansion,name='pansion'),
   
]
