from django.contrib import admin
from .models import *

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience', 'phone', 'email')
    search_fields = ('name', 'specialization')
    list_filter = ('specialization',)

admin.site.register(Doctor, DoctorAdmin)
