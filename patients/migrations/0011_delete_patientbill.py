# Generated by Django 4.0.6 on 2022-08-06 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0010_alter_patientbill_payment_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatientBill',
        ),
    ]
