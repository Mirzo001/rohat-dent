# Generated by Django 2.2 on 2020-07-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_auto_20200722_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]