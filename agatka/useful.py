from pages import models as page_models

from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.template import RequestContext
from django.contrib import messages
from .settings import MEDIA_ROOT

def base_context(request):
    isDark = request.COOKIES['isDark'] if ('isDark' in request.COOKIES) else False
    menu_tabs = page_models.MenuTab.objects.filter(is_a_logo = False, display = True).order_by('-priority')
    for tab in menu_tabs:
        try:
            tab.link = tab.page.friendly_link if not tab.is_external_link else tab.external_link
        except:
            tab.link = None
    
    logos_querry = page_models.MenuTab.objects.filter(is_a_logo = True, display = True)
    Logo = logos_querry[0] if logos_querry.count() > 0 else None
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
        page = page_models.Page.objects.filter(id_name=name)[0]
        ctx["page"] = page
        ctx["settings"] = page_models.PagesSetting.objects.filter(page=page)[0]
        ctx["title"] = page.title
        ctx["show_title"] = True
    except:
        pass
    return ctx