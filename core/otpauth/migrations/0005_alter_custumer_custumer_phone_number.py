# Generated by Django 4.1.7 on 2023-08-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpauth', '0004_alter_custumer_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custumer',
            name='custumer_phone_number',
            field=models.CharField(default='', max_length=10),
        ),
    ]
