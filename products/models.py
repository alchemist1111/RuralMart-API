from django.db import models

# Product model to represent products in the rural mart
class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True, default='product_images/default.jpg')
    product_image_url = models.URLField(blank=True, null=True)  # For external product image URLs
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Function to save the product image url in the database
    def save(self, *args, **kwargs):
        if self.product_image:
            self.product_image_url = self.product_image.url
        else:
            self.product_image_url = None
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} - {self.price}"
    
    
    
# Category model to represent product categories
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
