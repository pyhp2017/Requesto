from django.db import models
from django.contrib.auth.models import User

class Monitor(models.Model):
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    threshold = models.IntegerField()
    status = models.CharField(max_length=100,null=True, blank=True)
    number_of_fails = models.IntegerField(default=0)

    class Meta:
        unique_together = ('url', 'user',)

    def __str__(self):
        return self.url

class Request(models.Model):
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    result = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    counted = models.BooleanField(default=False)

    def __str__(self):
        return self.monitor.url
