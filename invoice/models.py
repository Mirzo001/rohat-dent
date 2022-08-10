
from django.db import models
from accounts.models import CustomUser
from patients.models import Patient
from django.utils import timezone
from django.utils.timezone import now

class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="bemor")
    # default=timezone.now bo'lsa unda user dateni kiritishiga to'g'ri kelyapti,
    # auto_now = True bo'lsa, user kiritmasdan saqlayapti lekin, o'zgartirib bo'lmayapti.
    date = models.DateTimeField(blank=True, auto_now = True)
    # due_date = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=False)
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.patient)
    
    def get_status(self):
        return self.status

    # def save(self, *args, **kwargs):
        # if not self.id:             
        #     self.due_date = datetime.datetime.now()+ datetime.timedelta(days=15)
        # return super(Invoice, self).save(*args, **kwargs)

class LineItem(models.Model):
    patient = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    

    def __str__(self):
        return str(self.patient)
    