from django.urls import path
from . import views

urlpatterns = [
       #  API endpoints 
    path('companies/', views.CompanyListCreateView.as_view(), name='company-list-create'),
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('devices/', views.DeviceListCreateView.as_view(), name='device-list-create'),
    path('device-logs/', views.DeviceLogListCreateView.as_view(), name='device-log-list-create'),
 
]
