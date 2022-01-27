from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserRegisterModel(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	dob=models.DateField(default=20)
	# address=models.TextField(max_length=90,default='abc')
	mobile_no=models.IntegerField(default=18)
	status=models.BooleanField(default=True)	
	created_on=models.DateTimeField(auto_now=True)

	def __str__(self):
		return (self.user.first_name+" "+self.user.last_name)
# Create your models here.

class BookModel(models.Model):
	user=models.CharField(max_length=30,default='none')
	hotel_booked=models.CharField(max_length=50,default='abc')
	room_type=models.CharField(max_length=100,default="none")
	price=models.IntegerField(default=1000)
	booking_date=models.DateField(default='2022-10-23')
	days=models.IntegerField(default=3)
	payment_status=models.BooleanField(default=False)
	created_on=models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.booking_date)

class AddFeedbackModel(models.Model):
	Name=models.CharField(max_length=50)
	Mail=models.CharField(max_length=50)
	Feedback=models.CharField(max_length=1000)
	status=models.BooleanField(default=True)
	created_on=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.Name
