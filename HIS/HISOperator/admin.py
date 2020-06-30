from django.contrib import admin

# Register your models here.

from .models import User


@admin.register(User)
class User_Admin(admin.ModelAdmin):
    list_display = ['userid', 'username', 'role']