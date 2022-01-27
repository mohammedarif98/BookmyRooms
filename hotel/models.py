from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class HotelDetailModel(models.Model):
	hotel_name=models.CharField(max_length=60,default="none")
	room_type=models.CharField(max_length=100,default="none")
	room_facility=models.CharField(max_length=500,default="none")
	price=models.IntegerField(default=1000)
	room_images=models.ImageField(upload_to="pics/",default="none")
	hotel_location=models.CharField(max_length=150,default="none")
	contact_no=models.IntegerField(default='988766544')
	email=models.EmailField(max_length=150)
	created_on=models.DateTimeField(auto_now=True)
	status=models.BooleanField(default=1)
	def __str__(self):
		return self.hotel_name




# Create your models here.
class HotelRegisterModel(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	contact_no=models.IntegerField(default=18)
	hotel_name=models.CharField(max_length=20,default="abc")
	hotel_image=models.ImageField(upload_to="pics/",default="none")
	status=models.BooleanField(default=True)	
	created_on=models.DateTimeField(auto_now=True)

	def __str__(self):
		return (self.user.first_name+" "+self.user.last_name)