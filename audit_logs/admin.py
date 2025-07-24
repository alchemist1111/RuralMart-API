from django.contrib import admin
from .models import AuditLog

# Register the AuditLog model with the admin site
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'action', 'object_id', 'object_repr')
    search_fields = ('user__first_name', 'action', 'object_repr')
    list_filter = ('action', 'timestamp')
    ordering = ('-timestamp',)
    date_hierarchy = 'timestamp'
