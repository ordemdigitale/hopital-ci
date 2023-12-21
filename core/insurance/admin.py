from django.contrib import admin

from core.insurance.models import Insurance


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address')
    list_filter = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Contact', {
            'fields': ('email', 'phone_number', 'address')
        }),
    )
