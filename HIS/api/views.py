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
    if request.method == 'POST':
        ci = checkitem.objects.values().distinct()
        return JsonResponse(list(ci), safe=False)

def getPatientByNo(request, pid):
    if request.method == 'POST':
        pat = patient.objects.filter(pid=pid).first()
        if pat:
            data = {
                'pid': pat.pid,
                'pname': pat.pname,
                'sex': pat.sex,
                'createDate': pat.createdate.strftime('%Y-%m-%d'),
                'idcard': pat.idcard,
                'level': {'levelname': pat.levelid.levelname},
                'pstatus': pat.pstatus,
                'dept': {'deptname': pat.deptid.deptname},
                'doc': {'dname': pat.doctorid.dname},
                }
            return JsonResponse(data)
        else:
            return JsonResponse({'pid': 0})

def saveCheckItemRecord(request, pid, dname):
    if request.method == 'POST':
        if len(request.POST) > 0:
            pat = patient.objects.filter(pid=pid).first()
        try:
            for k, v in request.POST.items():
                if 'cid' in k:
                    data = {
                        'pid': pat,
                        'cid': checkitem.objects.filter(id=int(v)).first(),
                        'amount': int(request.POST.get(k.replace('cid', 'amount'))),
                        'paystatus': 0,
                        }
                    checkitemrecord.objects.create(**data)
            return JsonResponse({'result': '提交检查申请成功'})
        except Exception:
            return JsonResponse({'result': '提交检查申请失败'})

# doctor_inspectitem
def getAllInspectItem(request):
    if request.method == 'POST':
        ii = inspectitem.objects.values().distinct()
        return JsonResponse(list(ii), safe=False)

def saveInspectItemRecord(request, pid, dname):
    if request.method == 'POST':
        if len(request.POST) > 0:
            pat = patient.objects.filter(pid=pid).first()
        try:
            for k, v in request.POST.items():
                if 'inspectid' in k:
                    data = {
                        'pid': pat,
                        'inspectid': inspectitem.objects.filter(id=int(v)).first(),
                        'amount': int(request.POST.get(k.replace('iid', 'amount'))),
                        'paystatus': 0,
                        }
                    inspectitemrecord.objects.create(**data)
            return JsonResponse({'result': '提交检验申请成功'})
        except Exception:
            return JsonResponse({'result': '提交检验申请失败'})

# doctor_medicalrecord
def getPatientDataByDoctor(request):
    if request.method == 'POST':
        pat = patient.objects.all()
        data = []
        for i in pat:
            data.append({
                'pid': i.pid,
                'pname': i.pname,
                'sex': i.sex,
                'createDate': i.createdate.strftime('%Y-%m-%d'),
                'idcard': i.idcard,
                'level': {'levelname': i.levelid.levelname},
                'pstatus': i.pstatus,
                'dept': {'deptname': i.deptid.deptname},
                'doc': {'dname': i.doctorid.dname},
                })
        return JsonResponse(data, safe=False)

# doctor_regmedicalrecord
def regMedicalRecord(request, pid):
    if request.method == 'POST':
        data = {
            'pid': patient.objects.filter(pid=pid).first(),
            'description': request.POST.get('description'),
            'medicalhistory': request.POST.get('medicalhistory'),
            'familyhistory': request.POST.get('familyhistory'),
            'initialresult': request.POST.get('initialresult')
            }
        data['status'] = 1
        data['operator'] = User.objects.filter(userid=request.session['userid']).first()
        medicalrecord.objects.create(**data)
        return JsonResponse({'result': '生成病例成功'})

# doctor_result
def getPatientAndMrData(request, pid):
    if request.method == 'POST':
        pat = patient.objects.filter(pid=pid).first()
        mr = medicalrecord.objects.filter(pid__pid=pid).last()
        if pat and mr:
            data = {
                'pid': pat.pid,
                'pname': pat.pname,
                'sex': pat.sex,
                'createDate': pat.createdate.strftime('%Y-%m-%d'),
                'idcard': pat.idcard,
                'level': {'levelname': pat.levelid.levelname},
                'pstatus': pat.pstatus,
                'dept': {'deptname': pat.deptid.deptname},
                'doc': {'dname': pat.doctorid.dname},
                'mr': {
                    'description': mr.description,
                    'medicalhistory': mr.medicalhistory,
                    'familyhistory': mr.familyhistory,
                    'initialresult': mr.initialresult,
                    'result': mr.result,
                    'finalresult': mr.finalresult,
                    'id': mr.id
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
        patient.objects.filter(medicalrecord__id=id).update(pstatus='已看诊')
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
            request.session['userrole'] = user.role
            return HttpResponse(role)
        else:
            return HttpResponse('error')

# outpatient_pay
def selectPatientByPno(request, pid):
    if request.method == 'POST':
        pat = patient.objects.filter(pid=pid).first()
        if pat:
            data = {
                'pid': pat.pid,
                'pname': pat.pname,
                'sex': pat.sex,
                'createDate': pat.createdate,
                'idcard': pat.idcard,
                'level': {'levelname': pat.levelid.levelname},
                'pstatus': pat.pstatus,
                'dept': {'deptname': pat.deptid.deptname},
                'doc': {'dname': pat.doctorid.dname},
                }
            data['cirList'] = []
            cir = checkitemrecord.objects.filter(pid__pid=pid)
            for item in cir:
                data['cirList'].append({
                    'paystatus': item.paystatus,
                    'id': item.id,
                    'checkItem': {
                        'itemname': item.cid.itemname,
                        'price': item.cid.price,
                        },
                    'amount': item.amount,
                    })
            data['iirList'] = []
            iir = inspectitemrecord.objects.filter(pid__pid=pid)
            for item in iir:
                data['iirList'].append({
                    'paystatus': item.paystatus,
                    'id': item.id,
                    'inspectItem': {
                        'inspectname': item.inspectid.inspectname,
                        'price': item.inspectid.price,
                        },
                    'amount': item.amount,
                    })
            return JsonResponse(data)
        else:
            return JsonResponse({'pid': 0})

def payItems(request):
    if request.method == 'POST':
        cid = [int(i) for i in request.POST.getlist('cid')]
        iid = [int(i) for i in request.POST.getlist('iid')]
        for id in cid:
            checkitemrecord.objects.filter(id=id).update(paystatus=1)
        for id in iid:
            inspectitemrecord.objects.filter(id=id).update(paystatus=1)
        return JsonResponse({'result': '缴费成功'})

# outpatient_refund
def refundPatient(request, pid):
    if request.method == 'POST':
        data = {
            'pstatus': '已退号',
            'status': 2,
            }
        patient.objects.filter(pid=pid).update(**data)
        return JsonResponse({'result': '退号成功'})

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
            data['status'] = 1
            data['pstatus'] = '未看诊'
            data['operator'] = User.objects.filter(userid=request.session['userid']).first()
            patient.objects.create(**data)
            return JsonResponse({'result': '挂号成功'})
        except Exception:
            return JsonResponse({'result': '挂号失败'})