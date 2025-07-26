from django.contrib import admin
from .models import Order, OrderItem

# Order model registration with the admin site
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'status', 'total_amount')
    search_fields = ('user__email', 'status')
    list_filter = ('status', 'order_date')

# OrderItem model registration with the admin site
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price')
    search_fields = ('order__id', 'product__name')
    list_filter = ('order',)
