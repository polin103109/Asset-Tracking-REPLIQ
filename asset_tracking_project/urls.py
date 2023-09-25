from rest_framework.schemas import get_schema_view

from django.contrib import admin
from django.urls import path, include
schema_view = get_schema_view(title='Corporate Asset Management API', public=True)

urlpatterns = [
    path('api/docs/', schema_view),
    path('admin/', admin.site.urls),
    path('api/', include('asset_tracking.urls')),
]
