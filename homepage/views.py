from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from . import models
from django.template import RequestContext
from django.contrib import messages
from agatka.useful import *
from images import models as images_models

def Homepage(request):
    ctx = set_navname("homepage", base_context(request))
    # messages.info(request, 'Your password has been changed successfully!')
    return render(request, "home.html", ctx)

def SetDarkMode(request):
    response = HttpResponse('darkness_cookie')
    response.set_cookie(key='isDark', value=request.GET['isDark'])
    return response

def Messeges(request):
    template = get_template("messages.html")
    content = template.render({}, request=request)
    return JsonResponse({"html":content})

def view_404(request, exception=None):
    return redirect('/')