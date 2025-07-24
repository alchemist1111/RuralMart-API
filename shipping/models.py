from django.db import models
from orders.models import Order

# Class to represent shipping information
class Shipping(models.Model):
    Order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipping_info')
    Shipping_address = models.CharField(max_length=255)
    tracking_number = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')
    shipping_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"Shipping Info for Order {self.Order.id} - Status: {self.status}"
