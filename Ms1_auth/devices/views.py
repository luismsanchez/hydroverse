from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import DeviceState, DeviceHistory
from .serializers import DeviceStateSerializer, DeviceHistorySerializer

# Device State

class DeviceStateListCreate(generics.ListCreateAPIView):
    queryset = DeviceState.objects.all()
    serializer_class = DeviceStateSerializer

class DeviceStateUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceState.objects.all()
    serializer_class = DeviceStateSerializer 

# Device History

class DeviceHistoryListCreate(generics.ListCreateAPIView):
    queryset = DeviceHistory.objects.all()
    serializer_class = DeviceHistorySerializer

class DeviceHistoryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceHistory.objects.all()
    serializer_class = DeviceHistorySerializer 