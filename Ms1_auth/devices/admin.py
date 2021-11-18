from django.contrib import admin
from .models import DeviceState, DeviceHistory

# Register your models here.

admin.site.register(DeviceState)
admin.site.register(DeviceHistory)
