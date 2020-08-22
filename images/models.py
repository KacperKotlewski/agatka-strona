from django.db import models
import os, uuid, io
from django.core.files import File

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Category(models.Model):
    visible_name = models.CharField(max_length=128, blank=True, null=True)
    friendly_link = models.CharField(max_length=128, unique=True)
    display = models.BooleanField(default=True)
    display_as_category = models.BooleanField(default=True)
    relase_date = models.DateTimeField()
    background_image = models.ImageField(_("background_image"), upload_to="pics/images", blank=True, null=True)

    def __str__(self):
        return "''"+self.visible_name+"''"
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

def get_upload_path_for_group(instance, filename):
    return 'pics/images/{0}/{1}'.format(instance.category.friendly_link, filename)
def get_upload_path_for_group_reduced_image(instance, filename):
    return 'pics/reducted_image/{0}/{1}'.format(instance.category.friendly_link, filename)
def get_upload_path_for_image(instance, filename):
    return 'pics/images/{0}/{1}/{2}'.format(instance.category.friendly_link, instance.group.friendly_link, filename)
def get_upload_path_for_reduced_image(instance, filename):
    return 'pics/reducted_image/{0}/{1}/{2}'.format(instance.category.friendly_link, instance.group.friendly_link, filename)

class Group(models.Model):
    visible_name = models.CharField(max_length=128, blank=True, null=True)
    friendly_link = models.CharField(max_length=128)
    display = models.BooleanField(default=True)
    relase_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    background_image = models.FileField(_("background_image"), upload_to=get_upload_path_for_group, blank=True, null=True)
    reducted_image = models.ImageField(_("reducted_image"), upload_to=get_upload_path_for_group_reduced_image, null=True, blank=True)

    def __str__(self):
        return "''"+self.visible_name + "'' z kategorii " +str(self.category)
    def save(self, *args, **kwargs):
        self.visible_name = (self.visible_name).replace("\"", "''")
        self.friendly_link = (self.friendly_link).replace("\"", "").replace("'", "")
        new_image = compress(self.background_image)
        self.reducted_image = new_image
        super().save(*args, **kwargs)

class Image(models.Model):
    visible_name = models.CharField(max_length=128, blank=True, null=True)
    friendly_link = models.CharField(max_length=128)
    display = models.BooleanField(default=True)
    relase_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to=get_upload_path_for_image)
    reducted_image = models.ImageField(_("reducted_image"), upload_to=get_upload_path_for_reduced_image, null=True, blank=True)

    def get_groups(self):
        groups = Group.objects.filter(category=self.category)
        return groups
    def __str__(self):
        return "''"+self.visible_name + "'' z grupy " +str(self.group)

    def create(self, **kwargs):
        obj = self.model(**kwargs)
        self._for_write = True
        return obj
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.reducted_image = new_image
        super().save(*args, **kwargs)


@receiver(post_delete, sender=Image)
@receiver(post_delete, sender=Group)
@receiver(post_delete, sender=Category)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if sender == Image:
        if instance.image:
            if os.path.isfile(instance.image.path):
                os.remove(instance.image.path)
    else:
        if instance.background_image:
            if os.path.isfile(instance.background_image.path):
                os.remove(instance.background_image.path)
    
    try:
        if instance.reducted_image:
            if os.path.isfile(instance.reducted_image.path):
                os.remove(instance.reducted_image.path)
    except: pass

@receiver(pre_save, sender=Image)
@receiver(pre_save, sender=Group)
@receiver(pre_save, sender=Category)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False


    try:
        if sender == Image:
            old_file = sender.objects.get(pk=instance.pk).image
        else:
            old_file = sender.objects.get(pk=instance.pk).background_image
    except sender.DoesNotExist:
        return False


    if sender == Image:
        new_file = instance.image
    else:
        new_file = instance.background_image
    try:
        if not (not old_file):
            if not old_file == new_file:
                if os.path.isfile(old_file.path):
                    os.remove(old_file.path)
    except: pass


    try:
        reduced_old_file = sender.objects.get(pk=instance.pk).reducted_image
        reduced_new_file = instance.reducted_image
        if not (not reduced_old_file):
            if not reduced_old_file == reduced_new_file:
                if os.path.isfile(reduced_old_file.path):
                    os.remove(reduced_old_file.path)
    except: pass


def compress(image):
    try:
        import Image
    except ImportError:
        from PIL import Image

    with Image.open(image) as im:
        size = im.size
        quality = 90
        if im.size[0] >=1200 or im.size[1] >=1200:
            size = (int(im.size[0]*0.5), int(im.size[1]*0.5))
        im_io = io.BytesIO() 
        im.thumbnail(size, Image.ANTIALIAS)
        while (int(im_io.tell()/1024) >= 80 or int(im_io.tell()) == 0):
            im_io = io.BytesIO()
            im.save(im_io, im.format, quality=quality) 
            quality -=5
        
        name = image.name.split('/')[-1]
        new_image = File(im_io, name= f'{name}')
        return new_image


def f(instance, filename):
    ext = filename.split('.')[-1]
    name = filename.split('/')[-1].split('.')[0]
    if instance.pk:
        return '{}.{}'.format(name, ext)
    else:
        pass