# Generated by Django 3.0.6 on 2020-05-13 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SEEUApp', '0005_auto_20200513_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
    ]
