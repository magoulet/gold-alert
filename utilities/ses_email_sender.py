import logging
import os

import boto3
from botocore.exceptions import ClientError

class EmailSender:
    def __init__(self, ses_client=None):
        self.region = os.environ.get('AWS_REGION', 'us-west-2')  # Fetch AWS region from environment variable
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        self.charset = "UTF-8"
        self.client = ses_client or boto3.client('ses', region_name=self.region)

    def send_email(self, subject, body_text, sender, recipient):
        """
        Send an email using AWS SES.

        Args:
        subject (str): The subject of the email.
        body_text (str): The body of the email.
        sender (str): The sender's email address.
        recipient (str): The recipient's email address.

        Returns:
        dict: A response with status code and message.
        """
        try:
            response = self.client.send_email(
                Destination={'ToAddresses': [recipient]},
                Message={
                    'Body': {'Text': {'Charset': self.charset, 'Data': body_text}},
                    'Subject': {'Charset': self.charset, 'Data': subject}
                },
                Source=sender
            )
        except ClientError as e:
            self.logger.error("Email not sent. Error: %s", e.response['Error']['Message'])
            return None
        else:
            self.logger.info("Email sent! Message ID: %s", response['MessageId'])
            return {"statusCode": 200, "message": "Email sent successfully"}
