import unittest
from app.services.a_where.a_where_services import AWhere
from Web.config import Config

class AuthTest(unittest.TestCase):
    def setUp(self):
        auth = AWhere(
            consumer_key=Config.A_WHERE_CONSUMER_KEY,
            consumer_secret=Config.A_WHERE_CONSUMER_SECRET
        )
        self.token = auth.authenticate()

    def test_authenticate_token(self):
        print("[INFO]: Token Received {}".format(self.token))
        self.assertEqual(len(self.token), 28)