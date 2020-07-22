from homepage import models as models_homepage

from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.template import RequestContext
from django.contrib import messages

def base_context(request):
    isDark = request.COOKIES['isDark'] if ('isDark' in request.COOKIES) else False
    menu_tabs = models_homepage.MenuTab.objects.filter(is_a_logo = False, display = True).order_by('-priority')
    for tab in menu_tabs:
        try:
            tab.link = tab.page.friendly_link if not tab.is_external_link else tab.external_link
        except:
            tab.link = None
    
    Logo = models_homepage.MenuTab.objects.filter(is_a_logo = True, display = True)[0]
    ctx = {
        "title" : "Agatka",
        "show_title" : False,
        "id_name" : "",
        "isDark" : isDark,
        "menu_tabs" : menu_tabs,
        "logo" : Logo,
        "settings": None,
        "page": None,
    }
    return ctx

def set_navname(name, ctx):
    ctx["id_name"] = name
    try:
        page = models_homepage.Page.objects.filter(id_name=name)[0]
        ctx["page"] = page
        ctx["settings"] = models_homepage.PagesSetting.objects.filter(page=page)[0]
        ctx["title"] = page.title
        ctx["show_title"] = True
    except:
        pass
    return ctx