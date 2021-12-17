from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

class Helper():
    """
    Provides DB Helper functions.

    Implements singleton pattern
    """
    _instance = None
    _session = None
    _engine = None
    _dbpath = None
    _base = None

    def __init__(self):
        raise RuntimeError("This is a singleton class. Use Helper.instance() instead.")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    def setDbPath(self, path):
        self._dbpath = path

    def getEngine(self):
        """
        get the SQLAlchemy engine

        :return: db engine
        """
        if(self._dbpath is None):
            raise Exception("Path to db must be set before calling this method")

        if(self._engine is None):
            self._engine = create_engine('sqlite:///' + self._dbpath)

        return self._engine

    def getSession(self):
        """
        Get a session to work with

        :return: Session for working with database
        """
        if(self._session is None):
            engine = self.getEngine()
            Session = sessionmaker(bind=engine)
            self._session = Session()

        return self._session

    def closeSession(self):
        """
        close a session
        """
        if(self._session is None):
            raise Exception("An session must be opened first (call getSession())")

        self._session.close()

    def getOrmBase(self):
        """
        Get the declarative base for ORM entities

        :return: SQLAlchemy declarative_base
        """
        if(self._base is None):
            self._base = declarative_base()

        return self._base

class CryptoEngine():
    """
    class to handle encryption and decryption of content

    :param password: password to encrypt and decrypt with
    :type password: str
    :param salt: salt for the password
    :type salt: str
    """
    _key = None

    def __init__(self, password, salt):
        """
        Constructor
        """
        if(isinstance(password, str) == False):
            raise TypeError("Password must be of type str")
        if(len(password) < 8):
            raise ValueError("Password should be at least 8 characters long")
        if(isinstance(salt, bytes) == False):
            raise TypeError("Salt must be of type bytes")
        if(len(salt) != 32):
            raise ValueError("Salt must be exactly 32 bytes long.")

        self._key = key = PBKDF2(password, salt, dkLen=32)

        

    def encrypt(self, data):
        """
        encrypt data with AES

        :param data: data to encrypt
        :type data: str

        :return: encrypted data
        :rtype: bytes (base64 encoded)
        """
        if(isinstance(data, str) == False):
            raise TypeError("Data to encrypt must be of type str")
        if(data == ""):
            raise ValueError("Data to encrypt should not be empty")

        data_bytes = bytes(data, 'utf-8')
        cipher = AES.new(self._key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data_bytes, AES.block_size))
        iv_length = (len(cipher.iv)).to_bytes(1,'big')

        return iv_length + cipher.iv + ct_bytes

    def decrypt(self, data):
        """
        decrypt data which was encrypted with AES

        :param data: data to decrypt
        :type data: bytes (base64)

        :return: decrypted data
        :rtype: str
        """
        if(isinstance(data, bytes) == False):
            raise TypeError("Data to decrypt must be of type bytes")
        if(data == ""):
            raise ValueError("Data to decrypt should not be empty")
        if(len(data) < 3):
            raise ValueError("Data must have at least three bytes (iv length, initialization vector and ciphertext)")

        iv_length = int(data[0])
        iv_bytes = data[1:1+iv_length]
        ct_bytes = data[1+iv_length:]
        cipher = AES.new(self._key, AES.MODE_CBC, iv_bytes)
        pt_bytes = unpad(cipher.decrypt(ct_bytes), AES.block_size)

        return pt_bytes.decode('utf-8')
