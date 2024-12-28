import urequests
import random

class APIHandler:
    """
    Handles interaction with an API to fetch data.
    """
    def __init__(self, url):
        """
        Initializes the API handler.

        :param url: The API endpoint URL.
        """
        self.url = url

    def get_random_conversion_rate(self):
        """
        Fetches random conversion rate data from the API.

        :return: A string representing the currency and its rate.
        """
        try:
            response = urequests.get(self.url)  # Fetch data from the API
            conversion_rates = response.json().get('conversion_rates', {})
            key, val = random.choice(list(conversion_rates.items()))
            return f"{key}: {val}"  # Format the result as 'Currency: Rate'
        finally:
            response.close()
