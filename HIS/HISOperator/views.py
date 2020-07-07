from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def login(request):
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return HttpResponse('1')
