from rest_framework import serializers
from .models import *


class MonitorSerializer(serializers.ModelSerializer):
    """
    Monitor serialization and validation
    """
    id = serializers.IntegerField(read_only=True)
    url = serializers.URLField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    threshold = serializers.IntegerField()
    status = serializers.CharField(read_only=True)
    number_of_fails = serializers.IntegerField(read_only=True)
    class Meta:
        model = Monitor
        fields = ('id', 'url', "user" ,'threshold', 'status', 'number_of_fails')

class RequestSerializer(serializers.ModelSerializer):
    """
    Request serialization and validation
    """
    monitor = MonitorSerializer()
    class Meta:
        model = Request
        fields = ('id', 'monitor', 'result', 'time')

    def create(self, validated_data):
        """
        submitting validated request data to database
        """
        try:
            request = Request.objects.create(**validated_data)
            request.save()
            return request
        except Exception:
            raise serializers.ValidationError({"message": 'There is something wrong during your request. Please try again later'})
