from django.db import models
from accounts.models import CustomUser
from products.models import Product

# Class to represent a product review
class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()  # Assuming rating is an integer from 1 to 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        
        ordering = ['-created_at']
        
    def __str__(self):
        return f'Review by: {self.user.first_name} {self.user.last_name} for {self.product.name} - Rating: {self.rating}'    
        
