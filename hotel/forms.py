
from django import forms
from hotel.models import HotelDetailModel,HotelRegisterModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class HotelDetailForm(forms.ModelForm):
	class Meta:
		model=HotelDetailModel
		exclude=("created_on",)


class HotelRegisterForm(UserCreationForm):
	class Meta:
		model=User
		fields=["username","first_name","last_name","password1","password2","email","is_staff"]

class ExtendedHotelForm(forms.ModelForm):
	class Meta:
		model=HotelRegisterModel
		fields=["contact_no","hotel_image","hotel_name"]

 


