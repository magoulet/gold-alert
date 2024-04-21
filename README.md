# Gold Price Alert

Gold Price Alert is a Python application that fetches the current gold price and sends an email notification if the price crosses a specified threshold based on a configurable trigger condition (above or below the threshold).

## Features

- Fetches the current gold price from the [GoldAPI.io](https://www.goldapi.io/) API.
- Sends an email notification using AWS SES (Simple Email Service) if the gold price crosses a configurable threshold.
- Configurable trigger condition (above or below the threshold) for sending notifications.
- Configurable email sender and recipient addresses.
- Logging for tracking application events.

## Prerequisites

- Python 3.6 or higher
- AWS account with SES configured and verified email addresses

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/magoulet/goldAlert.git
   ```

2. Navigate to the project directory:

   ```bash
   cd goldAlert
   ```

3. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure the application:

   - Rename the `config.toml.example` file to `config.toml`.
   - Open `config.toml` and update the following settings:
     - `gold_api.gold_api_key`: Your GoldAPI.io API key.
     - `thresholds.gold_threshold`: The gold price threshold for triggering notifications.
     - `thresholds.trigger_condition`: The trigger condition for sending notifications, either "above" or "below" the threshold. If trigger condition is set to "above", an email is sent if current price is above the threshold.  If trigger_condition is set to "below", an email is sent if current price is lower than the threshold.
     - `email_notifications.sender`: The email address from which the notifications will be sent.
     - `email_notifications.recipient`: The email address to which the notifications will be sent.

6. (Optional) Set up the run_gold_alert.sh script:

    - Rename the `run_gold_alert.sh.example` file to `run_gold_alert.sh`.
    Update the paths in the script to match your project directory and virtual environment location.
    - Mark the script as executable:
    ```text
    chmod +x run_gold_alert.sh
    ```



## Usage

To run the application, execute the following command:

```bash
python main.py
```

To set up a cron job to run the application once a day at 10 AM, follow these steps:

1. Open the cron table editor:
```text
crontab -e
```

Add a new line with the following entry:

```javascript

0 10 * * * /path/to/run_gold_alert.sh
```

Replace `/path/to/run_gold_alert.sh` with the actual path to the `run_gold_alert.sh` script on your system.

The application will fetch the current gold price and send an email notification if the price crosses the configured threshold based on the specified trigger condition.

## Testing

The application includes unit tests written using the `pytest` framework. To run the tests, execute the following command:

```bash
pytest
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
