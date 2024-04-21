import logging

import requests

from utilities.config import load_config

class GoldPriceAPI:
    def __init__(self):
        self.config = load_config()

        self.api_key = self.config["gold_api"]["gold_api_key"]
        self.base_url = "https://www.goldapi.io/api/"

        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def get_current_gold_price(self, symbol="XAU", curr="USD", date=""):
        try:
            url = f"{self.base_url}{symbol}/{curr}{date}"

            headers = {
                "x-access-token": self.api_key,
                "Content-Type": "application/json"
            }

            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            self.logger.info(data)
            return data
        except requests.RequestException as e:
            self.logger.error("An error occurred while making the Gold API request: %s", str(e))
            return None

