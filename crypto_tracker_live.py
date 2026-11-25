import time
import requests

def get_crypto_prices():

    print("\n===== LIVE CRYPTO MARKET TRACKER =====")
    print("Fetching latest market data...\n")

    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 5,
        "page": 1,
        "sparkline": "false"
    }

    try:
        response = requests.get(
            url, params=params, timeout=15
        )

        response.raise_for_status()

        data = response.json()

        print("Rank | Coin Name | Symbol | Price (USD)")
        print("------------------------------------------")

        for coin in data:
            print(
                coin["market_cap_rank"],
                "|", coin["name"],
                "|", coin["symbol"].upper(),
                "| $", coin["current_price"]
            )

        print("------------------------------------------")
        print("Market data fetched successfully!")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


while True:
    get_crypto_prices()
    print("\nRefreshing in 10 seconds...")
    time.sleep(10)
