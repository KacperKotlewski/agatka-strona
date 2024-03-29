# Generated by Django 3.0.5 on 2020-07-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20200723_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='pics/images'),
        ),
        migrations.AlterField(
            model_name='group',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='pics/images'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='pics/images'),
        ),
        migrations.AlterField(
            model_name='image',
            name='relase_date',
            field=models.DateTimeField(),
        ),
    ]
