from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import django.contrib.auth.validators
from .lists import BOOK_LANGUAGES, CATEGORIES

# Create your models here.

class CustomUser(AbstractUser):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 16 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=16, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])
    password = models.CharField(max_length=100, null=False)
    email = models.EmailField(blank=False, max_length=254, unique=True, null=False)
    phone_number = models.IntegerField(validators=[MinValueValidator(100000000), MaxValueValidator(999999999)], blank=True, null=True)
    
    profile_img = models.ImageField(upload_to='users', blank=True) 
    
    first_name = models.CharField(blank=False, max_length=50, null=False)
    surname = models.CharField(blank=False, max_length=50, null=False)
    last_name = models.CharField(blank=False, max_length=50, null=False)
    
    address = models.CharField(blank=False, max_length=250, null=False)
    
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"ID: {self.id} USER: {self.username} NAME: {self.first_name} {self.surname} {self.last_name}"

class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    isbn = models.BigIntegerField(validators=[MinValueValidator(1000000000000), MaxValueValidator(9999999999999)], unique=True)
    book_name = models.CharField(blank=False, max_length=50, null=False)
    author = models.CharField(blank=False, max_length=30, null=False)
    publisher = models.CharField(blank=False, max_length=15, null=False)
    
    languages = models.CharField(blank=False, max_length=20, choices=BOOK_LANGUAGES, null=False)
    
    description = models.TextField(blank=False, max_length=1500, null=False)
    
    image = models.ImageField(upload_to="books", blank=False)
    
    category = models.CharField(blank=False, max_length=20, choices=CATEGORIES, null=False)
    sub_category = models.CharField(blank=True, max_length=20, choices=CATEGORIES, null=True)
    
    is_new = models.BooleanField(default=True)
    on_sale = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)
    
    price = models.IntegerField(null=False)
    
    def __str__(self):
        return f"ID: {self.id} ISBN: {self.isbn} BOOK NAME: {self.book_name}"