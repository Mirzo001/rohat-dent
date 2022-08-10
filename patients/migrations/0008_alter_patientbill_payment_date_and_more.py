# Generated by Django 4.0.6 on 2022-08-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_patientbill_doctor_patientbill_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientbill',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='patientbill',
            name='status',
            field=models.CharField(choices=[("To'langan", "To'langan"), ("To'lanmagan", "To'lanmagan")], default="To'lanmagan", max_length=20),
        ),
    ]
