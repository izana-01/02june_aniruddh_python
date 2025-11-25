from django.contrib import admin
from .models import doctor

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'contact_number')
    search_fields = ('name', 'specialization')
    list_filter = ('specialization',)

admin.site.register(doctor, DoctorAdmin)