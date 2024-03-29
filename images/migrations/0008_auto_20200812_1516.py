# Generated by Django 3.0.5 on 2020-08-12 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0007_auto_20200810_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='background_image',
            field=models.FileField(blank=True, null=True, upload_to='<function get_upload_path_for_group at 0x03C51100>'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='<function get_upload_path_for_image at 0x03EBCF58>'),
        ),
    ]
