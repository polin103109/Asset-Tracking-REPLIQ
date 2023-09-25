
# Create your models here.
from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)  
    description = models.TextField()  
    def __str__(self):
        return f"{self.company_name} - {self.address}"

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=10,unique=True)
    employee_dept = models.CharField(max_length=100,null=True)
    employee_contact = models.CharField(max_length=15,null=True)
    employee_gender = models.CharField(max_length=50,null=True)
    def __str__(self):
          return f"ID: {self.employee_id}, Name: {self.employee_name}, Company:{self.company}, Dept: {self.employee_dept}, Contact: {self.employee_contact}, Gender: {self.employee_gender}"


class Device(models.Model):
    device_name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    condition = models.TextField()
    def __str__(self):
        return f"{self.device_name} ({self.serial_number})"

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_out_date = models.DateTimeField()
    check_in_date = models.DateTimeField(null=True, blank=True)
    condition_check_out = models.TextField()
    condition_check_in = models.TextField(null=True, blank=True)
   