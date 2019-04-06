from twilio.rest import Client
from config import Config

class TwilioCeres:
    def __init__(self, account_sid=None, auth_token=None):
        self.account_sid = account_sid
        self.auth_token = auth_token

    def authenitacte(self):
        return Client(self.account_sid, self.auth_token)





