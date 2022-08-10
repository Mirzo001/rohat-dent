# Generated by Django 4.0.6 on 2022-07-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_delete_patientvisit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientbill',
            name='treatment_date',
        ),
        migrations.AddField(
            model_name='patientbill',
            name='tolov_qaydlari',
            field=models.TextField(blank=True, default='', verbose_name="To'lov qaydlari"),
        ),
    ]
