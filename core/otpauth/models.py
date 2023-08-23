from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Custumer(models.Model):
    user = models.OneToOneField(User, related_name="custumer", on_delete=models.CASCADE)
    custumer_phone_number = models.CharField((""), max_length=10, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4())
    phone_otp = models.CharField("",max_length=4)

    def __str__(self) -> str:
        return self.user.username

