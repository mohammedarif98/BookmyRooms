# Generated by Django 3.2.9 on 2021-12-06 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_userregistermodel_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregistermodel',
            name='address',
        ),
    ]
