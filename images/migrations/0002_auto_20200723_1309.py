# Generated by Django 3.0.5 on 2020-07-23 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Group'),
        ),
    ]
