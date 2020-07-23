from agatka.useful import *
from . import models
from django.core import serializers
import base64
import os

def Images(request, image, category="none", group="none"):
    cat = models.Category.objects.filter(friendly_link=category)[0]
    grp = models.Group.objects.filter(friendly_link=group, category=cat)[0]
    img = models.Image.objects.filter(friendly_link=image, category=cat, group=grp)[0]
    ctx = {"img":img}
    return render(request, "image.html", ctx)