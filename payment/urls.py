from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment, name='payment_page'),
    path('handlerequest/', views.handlerequest, name='payment_handler')
]
