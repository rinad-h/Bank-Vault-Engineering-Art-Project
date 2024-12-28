import urequests
import random

def get_exchange_rate():
    """
    Fetch the latest exchange rates from the API and return a random conversion rate.
    Returns:
        res: A randomly selected exchange rate (key, value pair)
    """
    r = urequests.get("https://v6.exchangerate-api.com/v6/3caccaae69d659b02629d974/latest/CAD")
    conversion_rates = r.json().get('conversion_rates', {})  # Get the conversion rates from the API
    res = random.choice(list(conversion_rates.items()))  # Randomly select a conversion rate
    return res
