from django.urls import path
from .views import bitcoin_price

urlpatterns = [
    path('external/crypto/', bitcoin_price),
]
