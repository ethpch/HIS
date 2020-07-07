from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse


class HISInterceptor(MiddlewareMixin):
    def process_request(self, request):
        userrole = request.session.get('userrole', None)
        if not request.path.startswith('/api/') and not request.path.startswith('/logout'):
            if userrole == '门诊管理员' and not request.path.startswith('/outpatient'):
                return redirect(reverse('outpatient_register'))
            elif userrole == '医生管理员' and not request.path.startswith('/doctor'):
                return redirect(reverse('doctor_medicalrecord'))
            elif userrole == '系统管理员' and not request.path.startswith('/admin'):
                return redirect('admin:index')
            elif userrole is None and not request.path.startswith('/login'):
                return redirect(reverse('login'))
        