from django.contrib import admin
from .models import Payment

# Register payment model with the admin site
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_date', 'payment_method', 'amount', 'status')
    search_fields = ('order__id', 'payment_method')
    list_filter = ('status', 'payment_method', 'payment_date')