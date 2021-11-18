from .models import DeviceState, DeviceHistory
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class DeviceStateSerializer(serializers.ModelSerializer):
    #user = UserSerializer(read_only=True)
    class Meta:
        model = DeviceState
        fields = '__all__'
        
class DeviceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceHistory
        fields = '__all__'
