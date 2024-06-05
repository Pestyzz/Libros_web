from django.contrib import admin
from .models import CustomUser

# Register your models here.

class AdmUser(admin.ModelAdmin):
    list_display = ["id", "username", "first_name", "surname", "last_name", "phone_number", "is_active" , "is_staff"]

admin.site.register(CustomUser, AdmUser)