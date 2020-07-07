from django.shortcuts import render, redirect

# Create your views here.


from django.urls import reverse
from .models import *


def doctor_checkitem(request):
    return render(request, 'doctor_checkitem.html')

def doctor_inspectitem(request):
    return render(request, 'doctor_inspectitem.html')

def doctor_medicalrecord(request):
    return render(request, 'doctor_medicalrecord.html')

def doctor_regmedicalrecord(request):
    return render(request, 'doctor_regmedicalrecord.html')

def doctor_result(request):
    return render(request, 'doctor_result.html')

def outpatient_pay(request):
    return render(request, 'outpatient_pay.html')

def outpatient_refund(request):
    return render(request, 'outpatient_refund.html')

def outpatient_register(request):
    return render(request, 'outpatient_register.html')
