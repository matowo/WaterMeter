from .auth import TwilioCeres
from config import Config

class SendSMS(TwilioCeres):
    def __init__(self, account_sid=None, auth_token=None):
        TwilioCeres.__init__(self, account_sid, auth_token)
        self.client = self.authenitacte()

    def send_sms(self, to_number, body):
        message = self.client.messages.create(
            body=body, from_=Config.TWILIO_NUMBER,
            to=to_number
        )