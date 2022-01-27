from django.contrib import admin
from hotel.models import HotelDetailModel,HotelRegisterModel
# Register your models here.
admin.site.register(HotelDetailModel)
admin.site.register(HotelRegisterModel)