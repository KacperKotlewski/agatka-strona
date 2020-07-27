from django.db import models


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

    def __str__(self):
        return (str(self.page) + " settings")