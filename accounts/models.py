from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone

# Class for custom user manager
class CustomUserManager(BaseUserManager):
    """"
         Create and return a user with an email and password.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # Create a super user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

# Custom user model
class CustomUser(AbstractUser):
    # Role choices
    ROLES_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
        ('vendor', 'Vendor'),
    )
    username = None # Disable the default username
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True) # We will use email as the main authenticator
    phone_number = models.CharField(max_length=20, unique=True)
    roles = models.CharField(max_length=50, choices=ROLES_CHOICES, default='customer')  # e.g., customer, admin, vendor
    
    
    # Fields for use
    USERNAME_FIELD = 'email'  # Use email as the username field
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'roles'] # ields required for user creation
    
    objects = CustomUserManager()  # Use the custom user manager
    
    # Custom permissions
    class Meta:
        permissions = [
            # Profile permissions
            ("can_view_profile", "Can view user profile"),
            ("can_edit_profile", "Can edit user profile"),
            ("can_delete_profile", "Can delete user profile"),
            
            # Products permissions
            ("can_view_products", "Can view products"),
            ("can_add_product", "Can add product"),
            ("can_edit_product", "Can edit product"),
            ("can_delete_product", "Can delete product"),
            
            # Orders permissions
            ("can_view_orders", "Can view orders"),
            ("can_create_order", "Can create order"),
            ("can_edit_order", "Can edit order"),
            ("can_delete_order", "Can delete order"),
            
            # Cart permissions
            
            # User management permissions
            ("can_view_users", "Can view users"),
            ("can_add_user", "Can add user"),
            ("can_edit_user", "Can edit user"),
            ("can_delete_user", "Can delete user"),
        ]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
 
# User profile model   
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='userprofile')
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='profile_pics/default.jpg')
    profile_picture_url = models.URLField(blank=True, null=True)  # For external profile picture URLs
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Function to save the profile picture url in the database
    def save(self, *args, **kwargs):
        if self.profile_picture:
            self.profile_picture_url = self.profile_picture.url
        else:
            self.profile_picture_url = None
        super(UserProfile, self).save(*args, **kwargs)   
    
    
    def __str__(self):
        return f"Profile of {self.user.first_name} {self.user.last_name}"
        
