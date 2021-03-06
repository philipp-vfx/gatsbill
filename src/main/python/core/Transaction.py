from core.DBUtils import Helper
from core.Interfaces import Cryptable
from sqlalchemy import Column, String, Text, Date, ForeignKey
import uuid

Base = Helper.instance().getOrmBase()

class Transaction(Base, Cryptable):
    """
    Handles Transactions
    """

    __tablename__ = 'transactions'

    id = Column(String(36), primary_key=True)
    user = Column(String(36), ForeignKey('user.id'))
    _date = Column("date", Date)
    _currency = Column("currency", Text)
    _amount = Column("amount", Text)
    _creditorName = Column("creditor_name", Text)
    _creditorIban = Column("creditor_iban", Text)
    _debtorName = Column("deptor_name", Text)
    _debtorIban = Column("deptor_iban", Text)
    _transactionType = Column("transaction_type", Text)
    _description = Column("description", Text)
    _reference = Column("reference", Text)
    _invoice = Column("invoice", Text)

    def __init__(self):
        self.id = str(uuid.uuid4())

    def getDate(self):
        return self._date

    def setDate(self, date):
        self._date = date

    def getCurrency(self):
        return self.encryptedToText(self._currency)

    def setCurrency(self, currency):
        self._currency = self.textToEncrypted(currency)

    def getAmount(self):
        return self.encryptedToText(self._amount)

    def setAmount(self, amount):
        amountStr = str(amount)
        self._amount = self.textToEncrypted(amountStr)

    def getCreditorName(self):
        return self.encryptedToText(self._creditorName)

    def setCreditorName(self, creditor):
        self._creditorName = self.textToEncrypted(creditor)

    def getCreditorIban(self):
        return self.encryptedToText(self._creditorIban)

    def setCreditorIban(self, creditorIban):
        self._creditorIban = self.textToEncrypted(creditorIban)

    def getDebtorName(self):
        return self.encryptedToText(self._debtorName)

    def setDebtorName(self, debtor):
        self._debtorName = self.textToEncrypted(debtor)

    def getDebtorIban(self):
        return self.encryptedToText(self._debtorIban)

    def setDebtorIban(self, debtorIban):
        self._debtorIban = self.textToEncrypted(debtorIban)

    def getTransactionType(self):
        return self.encryptedToText(self._transactionType)

    def setTransactionType(self, type):
        self._transactionType = self.textToEncrypted(type)

    def getDescription(self):
        return self.encryptedToText(self._description)

    def setDescription(self, description):
        self._description = self.textToEncrypted(description)

    def getReference(self):
        return self.encryptedToText(self._reference)

    def setReference(self, reference):
        self._reference = self.textToEncrypted(reference)

    def getInvoice(self):
        return self.encryptedToText(self._invoice)

    def setInvoice(self, invoice):
        self._invoice = self.textToEncrypted(invoice)
