## PROJECT DETAIL

This is a project based on Django

## PROJECT DESCRIPTION

The web application utilizes Django for the backend development and Django REST Framework For building the API and SQLite database system for storing asset and user data, resulting in a robust and scalable solution that seamlessly handles data management.designed to help companies efficiently manage and track corporate assets such as phones, tablets, laptops, and other equipment distributed to employees. The application is designed to be flexible and scalable, allowing multiple companies to use it while maintaining their own asset records.

## 💻 Tech Stack

## backEnd

- Languages: [Django](https://docs.djangoproject.com/en/4.2/) -[Django Rest Framework](https://www.django-rest-framework.org/)

## Database

- SQLite

## ⌨️ Development

- First clone the repository by copy/paste the following command:

```bash
git clone git@github.com:polin103109/Asset-Tracking-REPLIQ.git
```

## Run Command(Backend)

- cd asset_tracking_project
  -python manage.py makemigrations
  -python manage.py migrate
  -python manage.py runserver

## Queries

- Query1:
  from asset_tracking.models import Device
  devices = Device.objects.filter(condition='Fully new')
  for device in devices:
  print(device.device_name)

-Query2:
from asset_tracking.models import DeviceLog, Employee
employee = Employee.objects.get(employee_id = '1601')  
device_logs = DeviceLog.objects.filter(employee=employee)

for log in device_logs:
print(f"Device: {log.device.device_name}, Check-Out Date: {log.check_out_date}, Check-In Date: {log.check_in_date}")

# Author

> Front-End Developer | Back-End Developer | React JS Developer | Node JS Developer | JavaScript Programmer

-Sabrina Sharmin

- `Linkedin` [Sabrina Sharmin](https://www.linkedin.com/in/sabrina-sharmin-937a441a7/)
- `Facebook` [Sabrina Sharmin](https://www.facebook.com/sharmin.polin/)
- `Email` [polinsharmin6@gmail.com](polinsharmin6@gmail.com)
