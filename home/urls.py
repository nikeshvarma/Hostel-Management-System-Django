from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('user/', views.userhome, name='userhome'),
    path('services/', views.services, name='service_page'),
]
