# Generated by Django 3.0.5 on 2020-08-09 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=128)),
                ('emial', models.EmailField(max_length=254)),
                ('topic', models.CharField(max_length=256)),
                ('message', models.TextField()),
            ],
        ),
    ]