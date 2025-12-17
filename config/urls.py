from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('campaigns.urls')),
    path('api/', include('external_api.urls')),
    path('api/', include('reports.urls')),
]
