# Generated by Django 3.0.5 on 2020-08-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200805_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='menutab',
            name='alternative_darkmode_image_for_logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo'),
        ),
        migrations.AddField(
            model_name='menutab',
            name='is_changing_with_darkmode',
            field=models.BooleanField(default=False),
        ),
    ]
