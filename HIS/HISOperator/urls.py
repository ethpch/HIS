﻿from django.urls import path, include
from django.views.generic import RedirectView
from .views import *


urlpatterns = [
    path('', RedirectView.as_view(url='login.html'), name='index'),
    path('login.html', login, name='login'),
    path('logout', logout, name='logout'),
    path('csrf_token', get_csrf),
    ]