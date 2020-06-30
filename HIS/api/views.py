from datetime import datetime


# Create your views here.

from django.http import HttpResponse, JsonResponse
from HISOperator.models import User
from hospital.models import *


# admin
def patient_dept_doctor(request):
    if request.method == 'POST':
        deptid = request.POST.get('deptid')
        if deptid:
            doctors = doctor.objects.filter(deptid=deptid).values_list('dname', flat=True)
        else:
            doctors = doctor.objects.all().values_list('dname', flat=True)
        return JsonResponse(list(doctors), safe=False)

# doctor_checkitem
def getAllCheckItem(request):
    return

def getPatientByNo(request, pid):
    return

def saveCheckItemRecord(request, pid, doctorid):
    return

# doctor_inspectitem
def getAllInspectItem(request):
    return

def saveInspectItemRecord(request, pid, doctorid):
    return

# doctor_medicalrecord
def getPatientDataByDoctor(request):
    return

# doctor_regmedicalrecord
def regMedicalRecord(request):
    return

# doctor_result
def getPatientAndMrData(request, pid):
    if request.method == 'POST':
        targetpat = patient.objects.filter(pid=pid).first()
        targetmr = medicalrecord.objects.filter(pid__pid=pid).first()
        if targetpat and targetmr:
            data = {
                'pid': targetmr.id,
                'pname': targetpat.pname,
                'sex': targetpat.sex,
                'createDate': targetpat.createdate.strftime('%Y-%m-%d'),
                'idcard': targetpat.idcard,
                'level': {'levelname': targetpat.levelid.levelname},
                'pstatus': targetpat.pstatus,
                'dept': {'deptname': targetpat.deptid.deptname},
                'doc': {'dname': targetpat.doctorid.dname},
                'mr': {
                    'description': targetmr.description,
                    'medicalhistory': targetmr.medicalhistory,
                    'familyhistory': targetmr.familyhistory,
                    'initialresult': targetmr.initialresult,
                    'result': targetmr.result,
                    'finalresult': targetmr.finalresult,
                    'id': targetmr.id
                    },
                }
            return JsonResponse(data)
        else:
            return JsonResponse({'pid': 0})

def updateMedicalRecord(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        data = {
            'result': request.POST.get('result'),
            'finalresult': request.POST.get('finalresult')
            }
        data['operator'] = User.objects.filter(userid=request.session['userid']).first()
        medicalrecord.objects.filter(id=id).update(**data)
        return JsonResponse({'result': '提交成功'})

# login
def selectRoles(request):
    roles = User.objects.values_list('role', flat=True).distinct()
    return JsonResponse(list(roles), safe=False)

def selectUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        user = User.objects.filter(username=username, password=password, role=role).first()
        if user:
            request.session['userid'] = user.userid
            return HttpResponse(role)
        else:
            return HttpResponse('error')

# outpatient_pay
def selectPatientByPno(request, pid):
    return

def payItems(request):
    return

# outpatient_refund
def refundPatient(request):
    return

# outpatient_register
def getPatientNo(request):
    if request.method == 'POST':
        pat = patient.objects.last()
        if pat:
            newpid = pat.pid + 1
        else:
            newpid = 1
        return JsonResponse({'pno': newpid})

def getLevelData(request):
    if request.method == 'POST':
        levs = level.objects.values().distinct()
        return JsonResponse(list(levs), safe=False)

def getDeptData(request):
    if request.method == 'POST':
        depts = dept.objects.values().distinct()
        return JsonResponse(list(depts), safe=False)

def getPatientData(request, pagesize, pagenum):
    if request.method == 'POST':
        patients = patient.objects.all()
        patients = [{
            'pid': item.pid,
            'pname': item.pname,
            'sex': item.sex,
            'idcard': item.idcard,
            'createDate': item.createdate.strftime('%Y-%m-%d'),
            'level': {'levelname': item.levelid.levelname},
            'pstatus': item.pstatus,
            'status': item.status,
            'dept': {'deptname': item.deptid.deptname},
            'doc': {'dname': item.doctorid.dname}
            } for item in patients]
        patients = [patients[i:i+pagesize] for i in range(0, len(patients), pagesize)]
        return JsonResponse(patients[pagenum-1], safe=False) if pagenum <= len(patients) else JsonResponse(list(), safe=False)

def getDoctorByDept(request, deptid):
    if request.method == 'POST':
        doctors = doctor.objects.filter(deptid=deptid)
        doctorsl = [{'id': doct.id, 'dname': doct.dname} for doct in doctors]
        return JsonResponse(doctorsl, safe=False)

def savePatient(request):
    if request.method == 'POST':
        try:
            data = {
                'pid': int(request.POST.get('pid')),
                'pname': request.POST.get('pname'),
                'sex': request.POST.get('sex'),
                'age': int(request.POST.get('age')) if request.POST.get('age') else None,
                'birthday': (request.POST.get('year') + '-' + request.POST.get('month')) if request.POST.get('year') and request.POST.get('month') else '',
                'idcard': int(request.POST.get('idcard')),
                'address': request.POST.get('address'),
                'levelid': level.objects.filter(id=int(request.POST.get('levelid'))).first(),
                'deptid': dept.objects.filter(id=int(request.POST.get('deptid'))).first(),
                'doctorid': doctor.objects.filter(id=int(request.POST.get('doctorid'))).first(),
                'createdate': datetime.strptime(request.POST.get('createDate'), '%Y-%m-%d'),
                'cost': int(request.POST.get('cost')),
                }
            data['status'] = 0
            data['pstatus'] = '未看诊'
            data['operator'] = User.objects.filter(userid=request.session['userid']).first()
            patient.objects.create(**data)
            return JsonResponse({'result': '挂号成功'})
        except Exception:
            return JsonResponse({'result': '挂号失败'})