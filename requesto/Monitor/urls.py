from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateMonitoringAPI.as_view()),
    path('list/', ListMonitoringAPI.as_view()),
    path('statistics/<int:pk>/', StatisticsAPI.as_view()),
    path('statistics/warnings/', WarningsAPI.as_view()),
]