from django.contrib import admin
from .models import Shipping


# Register shipping model with the admin site
admin.site.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('order', 'shipping_address', 'tracking_number', 'status', 'shipping_date')
    search_fields = ('order__id', 'tracking_number', 'shipping_address')
    list_filter = ('status', 'shipping_date')
