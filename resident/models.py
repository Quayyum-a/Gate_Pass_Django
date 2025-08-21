from django.contrib.auth.models import AbstractUser
from django.db import models

from resident.utility import generate_code


# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    is_resident = models.BooleanField(default=False)
    is_security = models.BooleanField(default=False)

class House(models.Model):
    house_number = models.PositiveIntegerField(unique=True)
    address = models.CharField(max_length=255, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class Invite(models.Model):
    code = models.CharField(max_length=10, unique=True, default=generate_code)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    house = models.ForeignKey(House, on_delete=models.PROTECT)

class Visit(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=True, null=False)
    phone = models.CharField(max_length=11, blank=False, null=False)
    invite  = models.ForeignKey(Invite, on_delete=models.PROTECT)