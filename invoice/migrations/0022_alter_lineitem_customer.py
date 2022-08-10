# Generated by Django 4.0.6 on 2022-08-06 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0010_alter_patientbill_payment_date'),
        ('invoice', '0021_alter_invoice_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient', verbose_name='bemor'),
        ),
    ]
