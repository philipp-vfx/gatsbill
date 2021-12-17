from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from core.DBUtils import Helper, CryptoEngine
from core.Transaction import Transaction
from Crypto.Random import get_random_bytes
import uuid
import bcrypt
import base64

Base = Helper.instance().getOrmBase()

class User(Base):
    """
    User Class to manage Users

    :param username: Username. This is used to identify a user and is safed in plain text.
    :type username: str
    :param firstName: first name of user
    :type firstName: str
    :param lastName: last name of user
    :type lastName: str
    :param password: password used to encrypt data. only hash will be safed.
    """
    __tablename__ = 'user'

    id = Column(String(36), primary_key=True)
    username = Column('username', Text)
    _firstName = Column('first_name', Text)
    _lastName = Column('last_name', Text)
    _passwordHash = Column('password_hash', Text)
    salt = Column('salt', Text)
    transactions = relationship("Transaction")

    _password = None

    def __init__(self, username, firstName, lastName, password):
        self.id = str(uuid.uuid4())
        self.salt = base64.b64encode(get_random_bytes(32)).decode('utf-8')
        cryptoEngine = CryptoEngine(password, self.getSalt())
        self.username = username
        self._firstName = base64.b64encode(
            cryptoEngine.encrypt(firstName)).decode('utf-8')
        self._lastName = base64.b64encode(
            cryptoEngine.encrypt(lastName)).decode('utf-8')
        self._passwordHash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode('utf-8')

        self._password = password

    def verifyPassword(self, password):
        return bcrypt.checkpw(password.encode(), self._passwordHash.encode())

    def setPassword(self, password):
        if(self.verifyPassword(password) == False):
            raise ValueError("The password is wrong for this user.")
        self._password = password

    def getFirstName(self):
        """
        Get first name in plain text
        """
        if(self._password == None):
            raise RuntimeError("Password must be set before calling this method. Call <User>.setPassword(<pwd>) first.")

        cryptoEngine = CryptoEngine(self._password, self.getSalt())
        return cryptoEngine.decrypt(base64.b64decode(self._firstName))

    def setFirstName(self, firstName):
        """
        set first name (encrypting it)
        """
        if(self._password == None):
            raise RuntimeError(
                "Password must be set before calling this method. Call <User>.setPassword(<pwd>) first.")

        cryptoEngine = CryptoEngine(self._password, self.getSalt())
        self._firstName = base64.b64encode(
            cryptoEngine.encrypt(firstName)).decode('utf-8')

    def getLastName(self):
        """
        Get last name in plain text
        """
        if(self._password == None):
            raise RuntimeError(
                "Password must be set before calling this method. Call <User>.setPassword(<pwd>) first.")

        cryptoEngine = CryptoEngine(self._password, self.getSalt())
        return cryptoEngine.decrypt(base64.b64decode(self._lastName))

    def setLastName(self, lastName):
        """
        set last name (encrypting it)
        """
        if(self._password == None):
            raise RuntimeError(
                "Password must be set before calling this method. Call <User>.setPassword(<pwd>) first.")

        cryptoEngine = CryptoEngine(self._password, self.getSalt())
        self._lastName = base64.b64encode(
            cryptoEngine.encrypt(lastName)).decode('utf-8')

    def getSalt(self):
        return base64.b64decode(self.salt)

    def addTransaction(self, transaction):
        """
        Add a transaction to the Users transactions

        :param transaction: transaction to add
        :type transaction: Transaction
        """
        if(isinstance(transaction, Transaction) == False):
            raise TypeError("Argument must be of type 'Transaction'")

        self.transactions.append(transaction)


