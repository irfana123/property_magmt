
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





# Create your models here.
