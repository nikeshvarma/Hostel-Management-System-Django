from django.contrib import admin
from .models import *
from django.contrib.admin import register


# Register your models here.


@register(Hostel)
class HostelManagementAdmin(admin.ModelAdmin):
    list_display = ('hostel_name',)
    search_fields = ('hostel_name',)


@register(Room)
class RoomManagementAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'capacity', 'hostel')
    search_fields = ('room',)
