# Generated by Django 3.0.5 on 2020-08-22 08:57

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0010_auto_20200812_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='reducted_image',
            field=models.ImageField(blank=True, null=True, upload_to=images.models.get_upload_path_for_reduced_image, verbose_name='reducted_image'),
        ),
    ]
