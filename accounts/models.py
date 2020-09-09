from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,blank=True,null=True,on_delete = models.CASCADE)
	first_name = models.CharField(max_length=200,null=True)
	last_name = models.CharField(max_length=200,null=True)
	phone = models.CharField(max_length=200,null=True)
	profile_pic = models.ImageField(default="profile_pics/default.jpg",null=True,blank=True,upload_to= "profile_pics")


	def __str__(self):
		return self.first_name
   

	def get_profile_pic(self):
		if self.profile_pic:
			return profile_pic_url
		else:
			return "profile_pics/default.jpg"

