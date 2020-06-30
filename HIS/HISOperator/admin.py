from django.contrib import admin

# Register your models here.

from .models import User
admin.site.site_title = 'HIS管理后台'
admin.site.site_header = 'HIS管理'


@admin.register(User)
class User_Admin(admin.ModelAdmin):
    list_display = ['userid', 'username', 'role']