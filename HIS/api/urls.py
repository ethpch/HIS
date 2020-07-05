from django.urls import path
from .views import *


urlpatterns = [
    # admin
    #path('patient_dept_doctor', patient_dept_doctor),
    # doctor_checkitem
    path('getAllCheckItem', getAllCheckItem),
    path('getPatientByNo/<int:pid>', getPatientByNo),
    path('saveCheckItemRecord/<int:pid>/<str:dname>', saveCheckItemRecord),
    # doctor_inspectitem
    path('getAllInspectItem', getAllInspectItem),
    #path('getPatientByNo/<int:pid>', getPatientByNo),
    path('saveInspectItemRecord/<int:pid>/<str:dname>', saveInspectItemRecord),
    # doctor_medicalrecord
    path('getPatientDataByDoctor', getPatientDataByDoctor),
    # doctor_regmedicalrecord
    #path('getPatientByNo/<int:pid>', getPatientByNo),
    path('regMedicalRecord/<int:pid>', regMedicalRecord),
    # doctor_result
    path('getPatientAndMrData/<int:pid>', getPatientAndMrData),
    path('updateMedicalRecord', updateMedicalRecord),
    # login
    path('selectRoles', selectRoles),
    path('selectUser', selectUser),
    # outpatient_pay
    path('selectPatientByPno/<int:pid>', selectPatientByPno),
    path('payItems', payItems),
    # outpatient_refund
    #path('getPatientByNo/<int:pid>', getPatientByNo),
    path('refundPatient/<int:pid>', refundPatient),
    # outpatient_register
    path('getPatientNo', getPatientNo),
    path('getLevelData', getLevelData),
    path('getDeptData', getDeptData),
    path('getPatientData/<int:pagesize>/<int:pagenum>', getPatientData),
    path('getDoctorByDept/<int:deptid>', getDoctorByDept),
    path('savePatient', savePatient),
    ]
