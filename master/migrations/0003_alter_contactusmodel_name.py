# Generated by Django 3.2.9 on 2021-12-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_alter_contactusmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusmodel',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
