
from tkinter import DISABLED
from django.db import models
from django.utils import timezone

from patients.models import Patient
from accounts.models import CustomUser



GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)

# STAFF_CHOICES = (
#     ("Dentist", "Dentist"),
#     ("Nurse", "Nurse"),
#     ("Dentist", "Technican"),
# )

# class BaseInfo(models.Model):
#     name = models.CharField(max_length=200)
#     phone = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200)
    
#     class Meta:
#         abstract = True
        
    

STATUS_CHOICES = (
    ("Yakunlandi", "Yakunlandi"),
    ("Kutilmoqda", "Kutilmoqda"),
    ("Bekor qilindi", "Bekor qilindi"),
)
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="bemor")
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now, verbose_name="sana")
    time = models.TimeField(default=timezone.now, verbose_name="vaqt")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    qaydlar = models.TextField(default='',blank=True)

    class Meta:
        ordering = ('time',)
        
   
    # def __str__(self):
    #     return self.date.strftime('%d %b %Y %H:%M:%S')
    def __str__(self):
        return self.time.strftime('%H:%M')
   
    
class Time(models.Model):
    time = models.TimeField()
    
    def __str__(self):
        return self.time.strftime('%H:%M')
    class Meta:
        ordering = ('time',)