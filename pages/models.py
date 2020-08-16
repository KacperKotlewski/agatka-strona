from django.db import models
import os
import uuid

from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class Page(models.Model):
    PAGE_TYPES = (
        ('home','hompage'),
        ('me','about me'),
        ('contact','contact'),
        ('portfolio','portfolio'),
    )

    id_name = models.CharField(max_length=128)
    page_title = models.CharField(max_length=128, blank=True, null=True)
    friendly_link = models.CharField(max_length=128, blank=True, null=True)
    page_types = models.CharField(max_length=64, choices=PAGE_TYPES, default='home')
    post_data = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.id_name

class MenuTab(models.Model):
    name = models.CharField(max_length=128)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True, null=True)
    is_external_link = models.BooleanField(default=False)
    external_link = models.CharField(max_length=128, blank=True, null=True)
    display = models.BooleanField(default=True)
    font_awesome_icon = models.CharField(max_length=128, blank=True, null=True)
    show_icon_only = models.BooleanField(default=False)
    is_a_logo = models.BooleanField(default=False)
    image_for_logo = models.ImageField(upload_to="logo", blank=True, null=True)
    is_changing_with_darkmode = models.BooleanField(default=False)
    alternative_darkmode_image_for_logo = models.ImageField(upload_to="logo", blank=True, null=True)
    to_new_tab = models.BooleanField(default=False)
    priority = models.DecimalField(default=0, decimal_places=0, max_digits=9999999)
    is_submenu = models.BooleanField(default=False)
    parent_menu = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class PagesSetting(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, blank=True, null=True)
    main_text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="logo", blank=True, null=True)
    image2 = models.ImageField(upload_to="logo", blank=True, null=True)

    def __str__(self):
        return (str(self.page) + " settings")




@receiver(models.signals.post_delete, sender=MenuTab)
@receiver(models.signals.post_delete, sender=PagesSetting)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if sender == MenuTab:
        if instance.image_for_logo:
            if os.path.isfile(instance.image_for_logo.path):
                os.remove(instance.image_for_logo.path)
        if instance.alternative_darkmode_image_for_logo:
            if os.path.isfile(instance.alternative_darkmode_image_for_logo.path):
                os.remove(instance.alternative_darkmode_image_for_logo.path)

    elif sender == PagesSetting:
        if instance.image:
            if os.path.isfile(instance.image.path):
                os.remove(instance.image.path)
        if instance.image2:
            if os.path.isfile(instance.image2.path):
                os.remove(instance.image2.path)

@receiver(models.signals.pre_save, sender=MenuTab)
@receiver(models.signals.pre_save, sender=PagesSetting)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        if sender == MenuTab:
            old_file1 = sender.objects.get(pk=instance.pk).image_for_logo
            old_file2 = sender.objects.get(pk=instance.pk).alternative_darkmode_image_for_logo
        elif sender == PagesSetting:
            old_file1 = sender.objects.get(pk=instance.pk).image
            old_file2 = sender.objects.get(pk=instance.pk).image2
    except sender.DoesNotExist:
        return False

    if sender == MenuTab:
        new_file1 = instance.image_for_logo
        new_file2 = instance.alternative_darkmode_image_for_logo
    elif sender == PagesSetting:
        new_file1 = instance.image
        new_file2 = instance.image2

    try:
        if not old_file1 == new_file1:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
        if not old_file2 == new_file2:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    except:
        pass