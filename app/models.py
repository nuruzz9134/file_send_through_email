from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from .manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    
    
    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def name(self):
        return self.first_name + ' ' + self.last_name

    def _str_(self):
        return self.email

    
