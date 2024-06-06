from django.contrib import admin
from .models import CustomUser, Book

# Register your models here.

class AdmUser(admin.ModelAdmin):
    list_display = ["id", "username", "first_name", "surname", "last_name", "phone_number", "is_active" , "is_staff"]

class AdmBook(admin.ModelAdmin):
    list_display = ["isbn", "book_name", "author", "publisher", "price"]

admin.site.register(CustomUser, AdmUser)
admin.site.register(Book, AdmBook)