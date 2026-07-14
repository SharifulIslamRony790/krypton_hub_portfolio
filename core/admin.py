from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Professional Django Admin for ContactMessage.
    Provides searching, filtering, and ordering.
    """
    list_display = ('name', 'email', 'company', 'service', 'created_at', 'is_read')
    list_filter = ('is_read', 'service', 'created_at')
    search_fields = ('name', 'email', 'company', 'message')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Contact Info', {
            'fields': ('name', 'email', 'company', 'phone')
        }),
        ('Message Details', {
            'fields': ('service', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )
