from django.shortcuts import render, redirect

# Create your views here.


from django.urls import reverse
from .models import *


def doctor_checkitem(request):
    if 'userid' in request.session.keys():
        return render(request, 'doctor_checkitem.html')
    else:
        return redirect(reverse('login'))

def doctor_inspectitem(request):
    if 'userid' in request.session.keys():
        return render(request, 'doctor_inspectitem.html')
    else:
        return redirect(reverse('login'))

def doctor_medicalrecord(request):
    if 'userid' in request.session.keys():
        return render(request, 'doctor_medicalrecord.html')
    else:
        return redirect(reverse('login'))

def doctor_regmedicalrecord(request):
    if 'userid' in request.session.keys():
        return render(request, 'doctor_regmedicalrecord.html')
    else:
        return redirect(reverse('login'))

def doctor_result(request):
    if 'userid' in request.session.keys():
        return render(request, 'doctor_result.html')
    else:
        return redirect(reverse('login'))

def outpatient_pay(request):
    if 'userid' in request.session.keys():
        return render(request, 'outpatient_pay.html')
    else:
        return redirect(reverse('login'))

def outpatient_refund(request):
    if 'userid' in request.session.keys():
        return render(request, 'outpatient_refund.html')
    else:
        return redirect(reverse('login'))

def outpatient_register(request):
    print(request.session.get_session_cookie_age())
    if 'userid' in request.session.keys():
        return render(request, 'outpatient_register.html')
    else:
        return redirect(reverse('login'))
