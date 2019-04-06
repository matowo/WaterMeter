import unittest
from app.services._twilio.auth import TwilioCeres
from app.services._twilio.send_sms import SendSMS
from config import Config

class SMSTest(unittest.TestCase):
    def setUp(self):
        sms = SendSMS(
            account_sid=Config.TWILIO_ACCOUNT_SID,
            auth_token=Config.TWILIO_AUTH_TOKEN
        )

        self.sms_test = sms.send_sms('+255714729460', 'Hi!')

    def test_send_sms(self):
        print("[INFO]: Send sms {}".format(self.sms_test))