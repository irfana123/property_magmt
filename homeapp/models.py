
from django.contrib.auth.models import AbstractUser
from django.db import models


class Login(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class company(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class users(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='users')
    name=models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name
class plan_details(models.Model):
    company=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='company_name')
    elevation=models.ImageField(blank=True,null=True)
    twod_plan=models.ImageField(blank=True,null=True)
    threed_plan=models.ImageField(blank=True,null=True)
    rooms=models.IntegerField(null=True,blank=True)
    bathrooms=models.IntegerField(null=True,blank=True)
    area=models.CharField(max_length=1000,null=True,blank=True)
    

class plan_request(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    company_name=models.ForeignKey(company,on_delete=models.CASCADE,blank=True,null=True)
    room=models.IntegerField(null=True,blank=True)
    bath=models.IntegerField(null=True,blank=True)
    area=models.CharField(max_length=1000,null=True,blank=True)
    additional=models.TextField(blank=True,null=True)
    budjet=models.IntegerField(null=True,blank=True)
    status=models.IntegerField(default=0)
    reply = models.FileField(blank=True, null=True)

class replyreq(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True,blank=True)
    company_name=models.OneToOneField(company,on_delete=models.CASCADE,null=True,blank=True)
    reply=models.FileField(blank=True,null=True)

class userComplaint(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    complaint = models.TextField()
    date = models.DateField()
    reply = models.TextField(null=True, blank=True)

    def __str__(self):
      return self.user



# Create your models here.
