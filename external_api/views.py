from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import fetch_bitcoin_price

@api_view(['GET'])
def bitcoin_price(request):
    data = fetch_bitcoin_price()
    return Response({
        "source": "CoinGecko",
        "bitcoin_price_usd": data["bitcoin"]["usd"]
    })
