from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

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
    email = models.EmailField(unique=True) # We will use email as the main authenticator
    phone_number = models.CharField(max_length=20, unique=True)
    roles = models.CharField(max_length=50, choices=ROLES_CHOICES, default='customer')  # e.g., customer, admin, vendor
    
    # Fields for use
    USERNAME_FIELD = 'email'  # Use email as the username field
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'roles'] # ields required for user creation
    
    objects = CustomUserManager()  # Use the custom user manager
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
 
# User profile model   
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='userprofile')
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    
    def __str__(self):
        return f"Profile of {self.user.first_name} {self.user.last_name}"
        
