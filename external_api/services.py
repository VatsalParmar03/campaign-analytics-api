import requests

def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        # If rate limited or any bad response
        if response.status_code != 200:
            return {
                "source": "CoinGecko",
                "bitcoin_price_usd": None,
                "status": "unavailable",
                "reason": f"External API returned {response.status_code}"
            }

        data = response.json()
        return {
            "source": "CoinGecko",
            "bitcoin_price_usd": data["bitcoin"]["usd"],
            "status": "success"
        }

    except Exception as e:
        return {
            "source": "CoinGecko",
            "bitcoin_price_usd": None,
            "status": "error",
            "reason": str(e)
        }
