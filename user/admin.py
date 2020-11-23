from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Profile)
class StudentProfile(admin.ModelAdmin):
    list_display = ['user', 'roll_no', 'course', 'apply', 'allotted', 'room', 'room_allocation_date']
    list_filter = ('roll_no', 'apply', 'course', 'allotted')
    search_fields = ('roll_no', 'name')
    actions = ('allotted',)

    def allotted(self, request, queryset):
        queryset.update(allotted=True)
        self.message_user(request, 'allotted room to selected profiles')

    allotted.short_description = 'Allot to selected profiles'
