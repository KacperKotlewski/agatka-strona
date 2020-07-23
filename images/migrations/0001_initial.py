# Generated by Django 3.0.5 on 2020-07-23 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible_name', models.CharField(blank=True, max_length=128, null=True)),
                ('friendly_link', models.CharField(max_length=128)),
                ('display', models.BooleanField(default=True)),
                ('display_as_category', models.BooleanField(default=True)),
                ('relase_date', models.DateTimeField(auto_now=True)),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='pics/main_images/categories')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible_name', models.CharField(blank=True, max_length=128, null=True)),
                ('friendly_link', models.CharField(max_length=128)),
                ('display', models.BooleanField(default=True)),
                ('relase_date', models.DateTimeField(auto_now=True)),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='pics/main_images/groups')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible_name', models.CharField(blank=True, max_length=128, null=True)),
                ('friendly_link', models.CharField(max_length=128)),
                ('display', models.BooleanField(default=True)),
                ('relase_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='pics')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Category')),
                ('group', models.ForeignKey(limit_choices_to={'category': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Category')}, on_delete=django.db.models.deletion.CASCADE, to='images.Group')),
            ],
        ),
    ]
