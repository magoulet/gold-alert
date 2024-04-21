import pytest
from unittest.mock import Mock, patch

from utilities.gold_price_api import GoldPriceAPI

@pytest.fixture
def gold_price_api():
    return GoldPriceAPI()

@patch('requests.get')
def test_get_current_gold_price(mock_get, gold_price_api):
    # Mock the response from the Gold API
    mock_response = Mock()
    mock_response.json.return_value = {"price": 1234.56}
    mock_get.return_value = mock_response

    result = gold_price_api.get_current_gold_price()
    assert result == mock_response.json()
