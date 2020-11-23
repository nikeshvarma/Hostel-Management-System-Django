from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile_page'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('room-application/', views.room_application, name='room_apply'),
    path('payment-complete/', views.payment_done, name='payment_done'),
]
