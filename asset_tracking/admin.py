from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(DeviceLog)
