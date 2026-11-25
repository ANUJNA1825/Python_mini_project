
import requests
import time

def get_crypto_prices():

    print("\n========== LIVE CRYPTO MARKET TRACKER ==========")
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
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()

        data = response.json()

        print(f"{'Coin':<15} {'Symbol':<8} {'Price (USD)':<16} {'24h Change'}")
        print("-" * 60)

        for coin in data:
            name = coin["name"]
            symbol = coin["symbol"].upper()
            price = coin["current_price"]
            change = coin["price_change_percentage_24h"]

            if change is not None:
                change_text = f"{change:+.2f}%"
            else:
                change_text = "N/A"

            print(f"{name:<15} {symbol:<8} ${price:<15,.4f} {change_text}")

        print("-" * 60)
        print("Market data fetched successfully!")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

while True:
    get_crypto_prices()
    print("\nRefreshing in 10 seconds...")
    time.sleep(10)
