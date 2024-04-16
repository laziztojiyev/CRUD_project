from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ImageField, CharField


# Create your models here.

class CustomUser(AbstractUser):
    image = ImageField(upload_to='users/')
    phone_number = CharField(max_length=25)


