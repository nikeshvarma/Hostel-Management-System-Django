from django.contrib import admin
from .models import HostelImages

admin.site.site_header = 'Admin Dashboard'


# Register your models here.

@admin.register(HostelImages)
class AdminImageManager(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)
