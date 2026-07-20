from django.contrib import admin
from .models import ContactMessage

# Admin Site Branding
admin.site.site_header = "Krypton 360 Admin Portal"
admin.site.site_title = "Krypton 360"
admin.site.index_title = "Welcome to the Lead Management Dashboard"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Premium Django Admin for ContactMessage using Custom UI.
    Provides searching, filtering, and ordering.
    """
    list_display = (
        'name',
        'email',
        'company',
        'service',
        'created_at',
        'is_read')
    list_filter = ('is_read', 'service', 'created_at')
    search_fields = ('name', 'email', 'company', 'message')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    list_editable = ('is_read',)

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

    actions = ['mark_as_read']

    @admin.action(description='Mark selected messages as read')
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f"{updated} message(s) successfully marked as read.")
