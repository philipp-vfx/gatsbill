from base64 import b64encode
from unittest import TestCase
import sys
import string
import random
sys.path.append("../main/python")
from core.DBUtils import CryptoEngine
from Crypto.Random import get_random_bytes


class Test(TestCase):

    def setUp(self):
        password = "password"
        salt = get_random_bytes(32)
        self.cryptoEngine = CryptoEngine(password, salt)

    def test_encryptionDecryption(self):
        message = "Hello World"
        encrypted = self.cryptoEngine.encrypt(message)

        self.assertFalse(encrypted == message)
        self.assertFalse(b64encode(encrypted).decode('utf-8') == message)

        decrypted = self.cryptoEngine.decrypt(encrypted)

        self.assertEquals(decrypted, message)

    def test_encryptionDecryptionLongData(self):
        s = string.ascii_lowercase + string.digits
        message = ''.join([random.choice(s) for _ in range(4096)])

        encrypted = self.cryptoEngine.encrypt(message)

        self.assertFalse(encrypted == message)
        self.assertFalse(b64encode(encrypted).decode('utf-8') == message)

        decrypted = self.cryptoEngine.decrypt(encrypted)

        self.assertEquals(decrypted, message)

    def test_encryptionDecryptionSpecialCharacters(self):
        message="@#*?\\/<>._-,;()=&%$"

        encrypted = self.cryptoEngine.encrypt(message)

        self.assertFalse(encrypted == message)
        self.assertFalse(b64encode(encrypted).decode('utf-8') == message)

        decrypted = self.cryptoEngine.decrypt(encrypted)

        self.assertEquals(decrypted, message)
