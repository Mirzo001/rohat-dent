# Generated by Django 4.0.6 on 2022-08-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0011_remove_invoice_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name="To'lov qaydlari"),
        ),
    ]