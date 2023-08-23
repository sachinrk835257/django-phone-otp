# Generated by Django 4.1.7 on 2023-08-23 17:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('otpauth', '0002_alter_custumer_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custumer',
            name='custumer_phone_number',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='custumer',
            name='phone_otp',
            field=models.CharField(default=' ', max_length=4),
        ),
        migrations.AlterField(
            model_name='custumer',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('3ab17254-744b-4ddd-b97f-aaf5b6c8ddec')),
        ),
    ]
