# Generated by Django 4.0.6 on 2022-07-25 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_patient_diagnoz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
    ]