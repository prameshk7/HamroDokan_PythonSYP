# Generated by Django 5.0.2 on 2024-03-29 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HamroDokan', '0007_remove_userprofilemodel_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofilemodel',
            name='is_vendor',
        ),
    ]
