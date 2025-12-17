from django.urls import path
from .views import campaign_summary

urlpatterns = [
    path('reports/campaign-summary/', campaign_summary),
]
