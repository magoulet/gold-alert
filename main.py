from utilities.config import load_config
from utilities.gold_price_api import GoldPriceAPI
from utilities.ses_email_sender import EmailSender


class GoldPriceFetcher:
    def __init__(self, gold_price_api, email_sender):
        self.gold_price_api = gold_price_api
        self.email_sender = email_sender

        # Load the configuration
        self.config = load_config()

    def fetch_price(self):
        try:
            # Make the request to get the gold price
            result = self.gold_price_api.get_current_gold_price()
            return result
        except Exception as e:
            print(f"An error occurred while fetching the gold price: {str(e)}")
            return None

    def process_response(self, result):
        if result and "price" in result:
            threshold =  self.config["thresholds"]["gold_threshold"]
            trigger_condition = self.config["thresholds"]["trigger_condition"]

        if trigger_condition == "below":
            if result["price"] < threshold:
                self.send_notification(result["price"])
            else:
                print(f"Gold price (${result['price']:.2f}) is above the threshold. No notification sent.")
        elif trigger_condition == "above":
            if result["price"] > threshold:
                self.send_notification(result["price"])
            else:
                print(f"Gold price (${result['price']:.2f}) is below the threshold. No notification sent.")
        else:
            print(f"Invalid trigger condition: {trigger_condition}")

    def send_notification(self, price):
        try:
            # Email notification
            subject = "Gold Price Alert"
            body_text = f"The gold price has crossed the threshold. The current price is ${price}."
            sender = self.config["email_notifications"]["sender"]
            recipient = self.config["email_notifications"]["recipient"]
            self.email_sender.send_email(subject, body_text, sender, recipient)
        except Exception as e:
            print(f"An error occurred while sending the email notification: {str(e)}")

if __name__ == "__main__":
    # Instantiate necessary objects
    gold_price_api = GoldPriceAPI()
    email_sender = EmailSender()

    # Instantiate GoldPriceFetcher
    gold_price_fetcher = GoldPriceFetcher(gold_price_api, email_sender)

    # Run the fetch_price and process_response methods
    result = gold_price_fetcher.fetch_price()

    # Mock response
    # result = {
        # "price": 2400
    # }

    gold_price_fetcher.process_response(result)