from core.DBUtils import CryptoEngine
import base64

class Cryptable():
    """
    Baseclass for encryptable and decryptable entities
    """

    cryptoEngine = None

    def initializeCryptoEngine(self, password, salt):
        """
        Initialize Crypto Engine. Must be called before any operation that need encryption or decryption
        """
        self.cryptoEngine = CryptoEngine(password, salt)

    def textToEncrypted(self, data):
        """
        Encrypt data and convert it to text that can be stored in database
        """
        if(self.cryptoEngine == None):
            raise RuntimeError("No crypt engine found. Call initializeCryptoEngine() before any other operation.")

        return base64.b64encode(self.cryptoEngine.encrypt(data)).decode('utf-8')

    def encryptedToText(self, data):
        """
        Decrypt data and convert it to string
        """
        if(self.cryptoEngine == None):
            raise RuntimeError("No crypt engine found. Call initializeCryptoEngine() before any other operation.")

        return self.cryptoEngine.decrypt(base64.b64decode(data))
