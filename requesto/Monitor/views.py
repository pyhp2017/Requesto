from rest_framework import generics
from .models import *
from .serializers import *
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CreateMonitoringAPI(generics.CreateAPIView):
    """
    Create monitoring
    """
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ListMonitoringAPI(generics.ListAPIView):
    """
    List monitoring
    """
    serializer_class = MonitorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Monitor.objects.filter(user=self.request.user)

class StatisticsAPI(generics.RetrieveAPIView):
    """
    Get statistics of a monitor
    """
    serializer_class = MonitorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Monitor.objects.all()

class WarningsAPI(generics.ListAPIView):
    """
    List warnings
    """
    serializer_class = MonitorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Monitor.objects.filter(status="Not Healthy")
