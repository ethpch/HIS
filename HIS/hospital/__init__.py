from django.apps import AppConfig


default_app_config = 'hospital.IndexConfig'
class IndexConfig(AppConfig):
    name = 'hospital'
    verbose_name = '医院数据系统'
