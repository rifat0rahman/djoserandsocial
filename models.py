from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=254,unique=True)
    REQUIRED_FIELDS = ['username','password']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

