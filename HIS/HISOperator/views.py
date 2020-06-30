from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.middleware.csrf import get_token
from .models import User

def login(request):
    if 'userid' in request.session.keys():
        role = User.objects.filter(userid=request.session['userid']).first().role
        if role == '门诊管理员':
            return redirect(reverse('outpatient_register'))
        elif role == '医生管理员':
            return redirect(reverse('doctor_medicalrecord'))
    else:
        return render(request, 'login.html')

def logout(request):
    request.session.pop('userid')
    return HttpResponse('1')

def get_csrf(request):
    return JsonResponse({'token': get_token(request)})
