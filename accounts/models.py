from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from config.settings import MEDIA_ROOT
STAFF_CHOICES = (
    ("Dentist", "Dentist"),
    ("Nurse", "Nurse"),
    ("Technican", "Technican"),
)

class CustomUser(AbstractUser):
    position = models.CharField(max_length=100, choices=STAFF_CHOICES, blank=True)
    profile_picture = models.ImageField(blank=True, default="default_profile_pic.jpg", upload_to='media')
    

