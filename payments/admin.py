from django.contrib import admin
from .models import Payment

# Register payment model with the admin site
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_amount', 'payment_method', 'payment_status', 'payment_date')
    search_fields = ('payment_date', 'payment_method')
    list_filter = ('payment_status', 'payment_method', 'payment_date')