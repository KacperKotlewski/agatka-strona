# Generated by Django 3.1 on 2020-09-05 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0014_group_reducted_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='position',
            field=models.IntegerField(default=1),
        ),
    ]
