import base64
import hashlib
from flask import g
# third party
from Crypto import Random
from Crypto.Cipher import AES
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as JWT
# local
from app import app
from app.users.models import User


jwt = JWT(app.config['SECRET_KEY'], expires_in=3600)
auth = HTTPTokenAuth('Bearer')


class AESCipher(object):

    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]


def generate_jwt(username):
    token = jwt.dumps({'username': username})
    return str(token)


def verify_password(username, password):
    try:
        user = User.objects(username=username).first()
        suite = AESCipher(app.config['SECRET_KEY'])
        our_password = suite.decrypt(user.password)
        if our_password == password:
            return user
    except:
        return None


@auth.verify_token
def verify_token(token):
    g.user = None
    try:
        data = jwt.loads(token)
    except:
        return False
    if 'username' in data:
        g.user = data['username']
        return True
    return False
