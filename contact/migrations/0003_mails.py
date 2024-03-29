# Generated by Django 3.0.5 on 2020-08-10 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0002_delete_mails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=128, verbose_name='Imię i nazwisko')),
                ('email', models.EmailField(max_length=254, verbose_name='E-Mail')),
                ('topic', models.CharField(max_length=256, verbose_name='Temat')),
                ('message', models.TextField(verbose_name='Wiadomość')),
            ],
        ),
    ]
