import requests
from requests.auth import HTTPBasicAuth
from Web.config import Config
from base64 import b64encode


class AWhere:


    def __init__(self, consumer_key=None, consumer_secret=None, base_url = 'https://api.awhere.com'):
        self.consumer_key=consumer_key
        self.consumer_secret=consumer_secret
        self.base_url = base_url
        self.encoded_key = self.encode_key(self.consumer_key, self.consumer_secret)


    def encode_key(self, key, secret):
        key_secret = '%s:%s'%(key, secret)
        return b64encode(bytes(key_secret, 'utf-8')).decode('ascii')

    def authenticate(self):
        authentication_uri = "/oauth/token"
        authentication_url = "{0}{1}".format(self.base_url, authentication_uri)

        print("KEY" + self.encoded_key)

        headers = {
            'Authorization': 'Basic {}'.format(self.encoded_key),
            'Content-Type': 'application/x-www-form-urlencoded'

        }

        body = "grant_type=client_credentials"


        r = requests.post(authentication_url, headers=headers, data=body)
        self.token = r.json()
        return r.json()