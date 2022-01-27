from django import forms
from master.models import ContactUsModel



class ContactUsForm(forms.ModelForm):
	class Meta:
		model=ContactUsModel
		exclude=("created_on",)