from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DeviceState(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    pump_state = models.BooleanField(default=False)
    comp_state = models.BooleanField(default=False)
    light_state = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(User)
    
    def __str__(self):
        return self.name


class DeviceHistory(models.Model):
    device_id = models.ForeignKey(DeviceState, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add = True)
    pump_state = models.BooleanField(default=False)
    comp_state = models.BooleanField(default=False)
    light_state = models.BooleanField(default=False)

    def __str__(self):
        return str(self.device_id) + " --> " + str(self.date)


