from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from . import models
from django.template import RequestContext
from django.contrib import messages
from agatka.useful import *
from images import models as images_models

def Portfolio(request, category=None, group=None):
    name = "portfolio"
    # messages.info(request, 'Your password has been changed successfully!')
    if category == None:
        ctx = set_navname(name, base_context(request))
        ctx["subcat"] = __getSubactegories(category)
        return render(request, "portfolio.html", ctx)
    else:
        from images import models as imgMod
        cat = imgMod.Category.objects.filter(friendly_link=category, display=True)[0]
        name = cat.visible_name
        ctx = set_navname(name, base_context(request))
        ctx["category"] = cat.friendly_link
        return render(request, "subcat.html", ctx)

def GetSubcategories(request):
    category = request.GET["category"] if request.method == 'GET' and 'category' in request.GET else None
    ctx = {"subcat":__getSubactegories(category)}
    return JsonResponse(ctx)

def __getSubactegories(category=None):
    from images import models as imgMod
    
    subcatTemp = None
    if category != None:
        cat = imgMod.Category.objects.filter(friendly_link=category, display=True)[0]
        subcatTemp = imgMod.Group.objects.filter(category=cat)
    else:
        subcatTemp = imgMod.Category.objects.filter(display_as_category=True, display=True)
    return list(subcatTemp)