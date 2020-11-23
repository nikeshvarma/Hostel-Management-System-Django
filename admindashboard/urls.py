from django.urls import path
from . import views

urlpatterns = [
    path('student-table/', views.student_table, name='table_page'),
    path('user-table/', views.user_table, name='user_table_page'),
    path('requested-user/', views.room_request, name='room_request_page'),
    path('room-allocation/<str:pk>/', views.room_allocation, name='allocation_page'),
    path('application-rejected/<str:pk>/', views.reject_application, name='application_reject'),
    path('delete-account/<str:username>/', views.delete_account, name='delete_account'),
    path('view-account/<str:username>/', views.view_profile, name='profile_view'),
    path('search/', views.search, name='search'),
]
