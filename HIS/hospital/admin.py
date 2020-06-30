from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(patient)
class patient_Admin(admin.ModelAdmin):
    list_display = ['pid', 'pname', 'sex', 'idcard', 'status']

    #class Media:
    #    js = (
    #        'js/jquery-3.2.1.min.js',
    #        'js/csrf_protect.js',
    #        'js/admin.js',
    #        )

@admin.register(level)
class level_Admin(admin.ModelAdmin):
    list_display = ['id', 'levelname']

@admin.register(dept)
class dept_Admin(admin.ModelAdmin):
    list_display = ['id', 'deptname']

@admin.register(doctor)
class doctor_Admin(admin.ModelAdmin):
    list_display = ['id', 'dname', 'deptid']

@admin.register(medicalrecord)
class medicalrecord_Admin(admin.ModelAdmin):
    list_display = ['id', 'status', 'operator']

@admin.register(checkitem)
class checkitem_Admin(admin.ModelAdmin):
    list_display = ['id', 'itemname']

@admin.register(checkitemrecord)
class checkitemrecord_Admin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(inspectitem)
class inspectitem_Admin(admin.ModelAdmin):
    list_display = ['id', 'inspectname']

@admin.register(inspectitemrecord)
class inspectitemrecord_Admin(admin.ModelAdmin):
    list_display = ['id']