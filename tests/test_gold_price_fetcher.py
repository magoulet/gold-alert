import pytest
from unittest.mock import Mock

from main import GoldPriceFetcher
from utilities.gold_price_api import GoldPriceAPI
from utilities.ses_email_sender import EmailSender

@pytest.fixture
def gold_price_fetcher():
    gold_price_api_mock = Mock(spec=GoldPriceAPI)
    email_sender_mock = Mock(spec=EmailSender)
    return GoldPriceFetcher(gold_price_api_mock, email_sender_mock)

def test_fetch_price(gold_price_fetcher):
    # Mock the response from the GoldPriceAPI
    mock_response = {"price": 1234.56}
    gold_price_fetcher.gold_price_api.get_current_gold_price.return_value = mock_response

    result = gold_price_fetcher.fetch_price()
    assert result == mock_response

def test_process_response_below_threshold(gold_price_fetcher):
    # Set the configuration
    gold_price_fetcher.config = {
        'thresholds': {
            'gold_threshold': 1500.0,
            'trigger_condition': 'below',
        },
        'email_notifications': {
            'sender': 'sender@example.com',
            'recipient': 'recipient@example.com'
        }
    }

    # Mock the response from the GoldPriceAPI
    mock_response = {"price": 1000.0}
    gold_price_fetcher.process_response(mock_response)

    # Assert that the email_sender.send_email method was called
    gold_price_fetcher.email_sender.send_email.assert_called()

def test_process_response_above_threshold(gold_price_fetcher):
    # Set the configuration
    gold_price_fetcher.config = {
        'thresholds': {
            'gold_threshold': 1500.0,
            'trigger_condition': 'below',
        },
        'email_notifications': {
            'sender': 'sender@example.com',
            'recipient': 'recipient@example.com'
        }
    }

    # Mock the response from the GoldPriceAPI
    mock_response = {"price": 2000.0}
    gold_price_fetcher.process_response(mock_response)

    # Assert that the email_sender.send_email method was not called
    gold_price_fetcher.email_sender.send_email.assert_not_called()

def test_process_response_above_threshold_trigger_above(gold_price_fetcher):
    # Set the configuration
    gold_price_fetcher.config = {
        'thresholds': {
            'gold_threshold': 1500.0,
            'trigger_condition': 'above',
        },
        'email_notifications': {
            'sender': 'sender@example.com',
            'recipient': 'recipient@example.com'
        }
    }

    # Mock the response from the GoldPriceAPI
    mock_response = {"price": 2000.0}
    gold_price_fetcher.process_response(mock_response)

    # Assert that the email_sender.send_email method was called
    gold_price_fetcher.email_sender.send_email.assert_called()
