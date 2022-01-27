# Generated by Django 3.2.9 on 2021-11-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=30)),
                ('room_images', models.ImageField(default='none', upload_to='pics/')),
                ('room_details', models.CharField(default='none', max_length=1000)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=1)),
            ],
        ),
    ]
