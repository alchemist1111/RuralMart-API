from django.contrib import admin
from .models import AuditLog

# Register the AuditLog model with the admin site
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action')
    search_fields = ('action', 'timestamp')
    list_filter = ('action', 'timestamp')
    ordering = ('-timestamp',)
    date_hierarchy = 'timestamp'
