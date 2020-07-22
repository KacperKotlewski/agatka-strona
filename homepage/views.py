from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from . import models
from django.template import RequestContext
from django.contrib import messages
from agatka.useful import *

def Homepage(request):
    ctx = set_navname("homepage", base_context(request))
    # messages.info(request, 'Your password has been changed successfully!')
    return render(request, "home.html", ctx)

def SetDarkMode(request):
    response = HttpResponse('darkness_cookie')
    response.set_cookie('isDark', request.GET['isDark'])
    data = {"success": True}
    return JsonResponse(data)