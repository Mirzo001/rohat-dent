# Generated by Django 4.0.6 on 2022-07-25 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_remove_appointment_diagnoz_appointment_qaydlar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='qaydlar',
            field=models.TextField(blank=True, default=''),
        ),
    ]
