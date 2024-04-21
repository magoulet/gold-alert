import pytest
from unittest.mock import Mock

from utilities.ses_email_sender import EmailSender

@pytest.fixture
def email_sender():
    mock_client = Mock()
    return EmailSender(ses_client=mock_client)

def test_send_email(email_sender):
    # Mock the successful response from the SES client
    mock_response = {'MessageId': 'test_message_id'}
    email_sender.client.send_email.return_value = mock_response

    subject = "Test Subject"
    body_text = "Test Body"
    sender = "sender@example.com"
    recipient = "recipient@example.com"

    response = email_sender.send_email(subject, body_text, sender, recipient)
    assert response == {"statusCode": 200, "message": "Email sent successfully"}
