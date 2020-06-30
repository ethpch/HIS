from django.urls import path
from .views import *


urlpatterns = [
    path('doctor_checkitem.html', doctor_checkitem, name='doctor_checkitem'),
    path('doctor_inspectitem.html', doctor_inspectitem, name='doctor_inspectitem'),
    path('doctor_medicalrecord.html', doctor_medicalrecord, name='doctor_medicalrecord'),
    path('doctor_regmedicalrecord.html', doctor_regmedicalrecord, name='doctor_regmedicalrecord'),
    path('doctor_result.html', doctor_result, name='doctor_result'),
    path('outpatient_pay.html', outpatient_pay, name='outpatient_pay'),
    path('outpatient_refund.html', outpatient_refund, name='outpatient_refund'),
    path('outpatient_register.html', outpatient_register, name='outpatient_register'),
    ]
