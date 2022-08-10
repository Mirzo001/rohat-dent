
from django.db import models
from django.utils import timezone

from accounts.models import CustomUser



class BaseInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name="ism")
    phone = models.CharField(max_length=200, verbose_name="telefon")
    address = models.CharField(max_length=200, default='', blank=True,verbose_name="manzil")
    
    class Meta:
        abstract = True

class Patient(BaseInfo):
    date_recorded = models.DateTimeField(default=timezone.now,verbose_name="yozilgan vaqti")
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    diagnoz = models.TextField(default='',blank=True)
    
    def __str__(self):
        return self.name
    

# class PatientVisit(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     visit_date = models.DateTimeField(default=timezone.now)
#     visit_amount = models.IntegerField(null=True)

#     def __str__(self):
#         return self.patient.name
    
# class PatientBill(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="bemor")
#     amount = models.FloatField()
#     payment_date = models.DateTimeField(default=timezone.now)
#     tolov_qaydlari = models.TextField(default='', blank=True, verbose_name="To'lov qaydlari")
    
#     def __str__(self):
#         return self.patient.name
