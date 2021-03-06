# Generated by Django 3.2.9 on 2021-12-09 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_bookmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='check_in_date',
        ),
        migrations.RemoveField(
            model_name='bookmodel',
            name='check_out_date',
        ),
        migrations.RemoveField(
            model_name='bookmodel',
            name='name',
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='booking_date',
            field=models.DateField(default='2022-10-23'),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='days',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='hotel_booked',
            field=models.CharField(default='abc', max_length=50),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='price',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='room_type',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='user',
            field=models.CharField(default='none', max_length=30),
        ),
    ]
