import time
from django.core.management.base import BaseCommand
from datetime import datetime
from Monitor.models import Monitor, Request
import requests

class Command(BaseCommand):
    help = 'Update the status of the requests'

    def add_arguments(self, parser):
        parser.add_argument('time_interval', type=int, default=10)

    # this is a staticmethod which sends requests for all the Monitor Objects.
    # then it will update number of fails and status
    @staticmethod
    def send_requests():
        print("Sending requests at: ", datetime.now())
        monitors = Monitor.objects.all()
        for monitor in monitors:
            print(monitor.url)
            status = 200
            try:
                url_request = requests.get(monitor.url, verify=False)
                status = url_request.status_code
            except Exception:
                status = 503
            Request.objects.create(monitor=monitor, result=status)

        
        print("Update the number of fails at: ", datetime.now())
        all_requests = Request.objects.all()
        for request in all_requests:
            if request.result < 200 or request.result > 299:
                if not request.counted:
                    request.monitor.number_of_fails += 1
                    request.monitor.save()
                    request.counted = True
                    request.save()
            if request.monitor.number_of_fails >= request.monitor.threshold:
                request.monitor.status = "Not Healthy"
                request.monitor.save()

    # Handle Command
    def handle(self, *args, **options):
        time_interval = options['time_interval']
        while True:
            # Repeat this until killing the process
            Command.send_requests()
            # sleept with specific time interval
            time.sleep(time_interval)
