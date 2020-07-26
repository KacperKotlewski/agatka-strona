from agatka.useful import *
from . import models
from django.core import serializers
import base64
import os

def Images(request, image, category="none", group="none"):
    img = filterImages(image=image, category=category, group=group)[0]
    ctx = {"img":img.image.url}
    return JsonResponse(ctx)

def GetImages(request):
    category = request.GET["category"] if request.method == 'GET' and 'category' in request.GET else None
    group = request.GET["group"] if request.method == 'GET' and 'group' in request.GET else None
    count = int(request.GET["count"]) if request.method == 'GET' and 'count' in request.GET else 1

    imgs = filterImages(category=category, group=group)
    images = []
    for i in range(count):
        if len(imgs) <= i:
            break
        else:
            images.append({"id":imgs[i].id,"url":imgs[i].image.url})

    ctx = {"imgs":images}
    return JsonResponse(ctx)

def filterImages(category=None, group=None, image=None):
    from django.utils.timezone import now
    cat = None
    grp = None
    imgs = None

    if category != None:
        cat = models.Category.objects.filter(friendly_link=category)[0]
    if group != None:
        if cat != None:
            grp = models.Group.objects.filter(friendly_link=group, category=cat)[0]
        else:
            grp = models.Group.objects.filter(friendly_link=group)[0]
    if image != None:
        if cat != None:
            if grp != None:
                imgs = models.Image.objects.filter(friendly_link=image, category=cat, group=grp)
            else:
                imgs = models.Image.objects.filter(friendly_link=image, category=cat)
        else:
            if grp != None:
                imgs = models.Image.objects.filter(friendly_link=image, group=grp)
            else:
                imgs = models.Image.objects.filter(friendly_link=image)
    else:
        if cat != None:
            if grp != None:
                imgs = models.Image.objects.filter(category=cat, group=grp)
            else:
                imgs = models.Image.objects.filter(category=cat)
        else:
            if grp != None:
                imgs = models.Image.objects.filter(group=grp)
            else:
                imgs = models.Image.objects.filter()

    return imgs.order_by('-relase_date')