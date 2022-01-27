from django.db import models


class ContactUsModel(models.Model):
	name=models.CharField(max_length=20)
	email=models.CharField(max_length=40)
	message=models.TextField()
	# status=models.BooleanField(default=1)
	created_on=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

# Create your models here.
