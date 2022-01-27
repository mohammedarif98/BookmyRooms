# Generated by Django 3.2.9 on 2021-12-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_alter_hoteldetailmodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelregistermodel',
            name='hotel_name',
            field=models.CharField(default='abc', max_length=20),
        ),
        migrations.AlterField(
            model_name='hoteldetailmodel',
            name='email',
            field=models.EmailField(max_length=150),
        ),
    ]