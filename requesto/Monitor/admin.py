from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    pass

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)
