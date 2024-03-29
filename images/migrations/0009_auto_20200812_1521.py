# Generated by Django 3.0.5 on 2020-08-12 13:21

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0008_auto_20200812_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='background_image',
            field=models.FileField(blank=True, null=True, upload_to=images.models.get_upload_path_for_group),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=images.models.get_upload_path_for_image),
        ),
    ]
