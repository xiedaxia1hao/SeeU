# Generated by Django 3.0.6 on 2020-05-13 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SEEUApp', '0004_auto_20200513_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='email',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='password',
            field=models.CharField(default=True, max_length=16),
            preserve_default=False,
        ),
    ]
