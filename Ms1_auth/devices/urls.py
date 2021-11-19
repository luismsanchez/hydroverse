from django.urls import path, include
from .views import *

urlpatterns = [
    path('registration/', DeviceStateListCreate.as_view()),
    path('registration/<pk>/', DeviceStateUpdateDelete.as_view()),
    path('history/', DeviceHistoryListCreate.as_view()),
    path('history/<pk>/', DeviceHistoryUpdateDelete.as_view()),
]
