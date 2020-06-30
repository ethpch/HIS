from django.shortcuts import render, redirect

# Create your views here.


from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.middleware.csrf import get_token

def login(request):
    if 'userrole' in request.session.keys():
        role = request.session['userrole']
        if role == '门诊管理员':
            return redirect(reverse('outpatient_register'))
        elif role == '医生管理员':
            return redirect(reverse('doctor_medicalrecord'))
        elif role == '系统管理员':
            pass
    else:
        return render(request, 'login.html')

def logout(request):
    request.session.clear()
    return HttpResponse('1')

def get_csrf(request):
    return JsonResponse({'token': get_token(request)})
