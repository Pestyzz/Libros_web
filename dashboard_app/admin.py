from django.contrib import admin
from .models import CustomUser, Book, Shopping, ShoppingItem

# Register your models here.

class AdmUser(admin.ModelAdmin):
    list_display = ["id", "username", "first_name", "surname", "last_name", "phone_number", "is_active" , "is_staff"]

class AdmBook(admin.ModelAdmin):
    list_display = ["isbn", "book_name", "author", "publisher", "price"]
    
class AdmShopping(admin.ModelAdmin):
    list_display = ["id", "client", "paid", "status", "creation_date"]
    
class AdmShoppingItem(admin.ModelAdmin):
    list_display = ["shopping", "product_id", "quantity"]

admin.site.register(CustomUser, AdmUser)
admin.site.register(Book, AdmBook)
admin.site.register(Shopping, AdmShopping)
admin.site.register(ShoppingItem, AdmShoppingItem)