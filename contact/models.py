from django.db import models
import django.forms as forms

class Mails(models.Model):
    names = models.CharField(max_length=128, verbose_name=u"Imię i nazwisko")
    email = models.EmailField(verbose_name=u"E-Mail")
    topic = models.CharField(max_length=256, verbose_name=u"Temat")
    message = models.TextField(verbose_name=u"Wiadomość")