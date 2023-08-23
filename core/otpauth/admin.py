from django.contrib import admin
from .models import Custumer
# Register your models here.
class CustumerAdmin(admin.ModelAdmin):
    list_display = ["id","uuid"]

admin.site.register(Custumer,CustumerAdmin)
