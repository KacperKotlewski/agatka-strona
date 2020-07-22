from django.shortcuts import render, redirect, HttpResponse
from . import models
from django.template import RequestContext

def Homepage(request):
    ctx = base_context(request)
    ctx["show_title"] = True
    ctx["nav_name"] = "Home"
    return render(request, "home.html", ctx)

def SetDarkMode(request):
    response = HttpResponse('darkness_cookie')
    response.set_cookie('isDark', request.GET['isDark'])
    return response



def base_context(request):
    isDark = request.COOKIES['isDark'] if ('isDark' in request.COOKIES) else False
    # menu_tabs = models.MenuTabs.objects.all()
    ctx = {
        "title" : "Agatka",
        "show_title" : False,
        "nav_name" : "",
        "isDark" : isDark,
        # "menu_tabs" : menu_tabs,
    }
    return ctx