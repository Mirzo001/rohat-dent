# Generated by Django 4.0.6 on 2022-08-05 17:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_remove_patientbill_treatment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='manzil'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_recorded',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='yozilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=200, verbose_name='ism'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=200, verbose_name='telefon'),
        ),
        migrations.AlterField(
            model_name='patientbill',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient', verbose_name='bemor'),
        ),
    ]
