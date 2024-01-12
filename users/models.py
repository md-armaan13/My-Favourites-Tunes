from django.db import models
from django.contrib.auth.models import AbstractUser



class Users (AbstractUser):
    username = models.CharField(max_length=150, unique=False, blank=True)
    email = models.EmailField(unique=True)  

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']
