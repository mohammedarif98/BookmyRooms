# Generated by Django 3.2.9 on 2021-12-13 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_remove_hotelregistermodel_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelregistermodel',
            name='Hotel_name',
            field=models.CharField(default='abc', max_length=20),
        ),
    ]
