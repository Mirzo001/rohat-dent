# Generated by Django 4.0.6 on 2022-08-05 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0018_invoice_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='doctor',
        ),
    ]