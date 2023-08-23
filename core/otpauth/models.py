from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Custumer(models.Model):
    user = models.OneToOneField(User, related_name="custumer", on_delete=models.CASCADE)
    custumer_phone_number = models.CharField(max_length=10, default="")
    uuid = models.CharField(max_length=255, default=" ")
    phone_otp = models.CharField(default=" ", max_length=4)

    def __str__(self) -> str:
        return self.custumer_phone_number

