# Generated by Django 4.0.6 on 2022-08-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0026_alter_invoice_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]