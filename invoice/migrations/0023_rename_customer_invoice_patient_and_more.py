# Generated by Django 4.0.6 on 2022-08-06 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0022_alter_lineitem_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='customer',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='lineitem',
            old_name='customer',
            new_name='patient',
        ),
    ]
