from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
from master.forms import ContactUsForm
from master.models import ContactUsModel

class AboutusView(TemplateView):
	template_name="aboutus.html"

class HomeView(TemplateView):
	template_name="bookmyrooms.html"

class ContactUsView(CreateView):
	template_name="contactus.html"
	form_class=ContactUsForm
	success_url="/master/bookmyrooms/"

class ContactUsList(ListView):
	template_name="contactuslist.html"
	model=ContactUsModel
	context_object_name="contactlist"

class AdminHome(TemplateView):
	template_name="adminhome.html"

# Create your views here.
