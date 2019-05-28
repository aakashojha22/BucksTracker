from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your models here.



class UserInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_active= models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)
    salary = models.PositiveIntegerField(blank=True)
    mobile_no = models.IntegerField(blank=True)



    def get_absolute_url(self):
        return redirect("thankyou")

    def __str__(self):
        return  self.user.username

