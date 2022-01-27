from django import forms
from user.models import*
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets

from django import forms

class UserRegisterForm(UserCreationForm):
	class Meta:
		model=User
		fields=["username","first_name","last_name","password1","password2","email"]

class ExtendedUserForm(forms.ModelForm):
	class Meta:
		model=UserRegisterModel
		fields=["dob","mobile_no"]



class Subscribe(forms.Form):
	Email = forms.EmailField()
	def __str__(self):
		return self.Email


class DateInput(forms.DateInput):
	input_type="date"


class BookForm(forms.ModelForm):
	class Meta:
		model=BookModel
		fields=('booking_date','days')
		widgets={

			'booking_date':DateInput()
		}

class AddFeedbackForm(forms.ModelForm):
	class Meta:
		model=AddFeedbackModel
		exclude=("created_on","status",)
