from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from . import models
from django.template import RequestContext
from django.contrib import messages
from agatka.useful import *
from images import models as images_models

def Portfolio(request, category=None):
    name = "portfolio"
    ctx = set_navname(name, base_context(request))
    # messages.info(request, 'Your password has been changed successfully!')
    return render(request, "portfolio.html", ctx)