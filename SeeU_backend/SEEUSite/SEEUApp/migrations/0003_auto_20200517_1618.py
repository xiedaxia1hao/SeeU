# Generated by Django 3.0.6 on 2020-05-17 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SEEUApp', '0002_delete_user_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seeu_user',
            name='sex',
            field=models.CharField(max_length=10),
        ),
    ]
