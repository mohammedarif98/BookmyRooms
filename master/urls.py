from django.urls import path
from master.views import AboutusView,HomeView,ContactUsView,ContactUsList,AdminHome
from master import views

urlpatterns=[
			path("aboutus/",AboutusView.as_view(),name='aboutus'),
			path('bookmyrooms/',HomeView.as_view(),name="bookmyrooms"),
			path("contactus/",ContactUsView.as_view(),name="contactus"),
			path("contactuslist/",ContactUsList.as_view(),name="contactuslist"),
			path('adminhome/',AdminHome.as_view(),name="adminhome")

]