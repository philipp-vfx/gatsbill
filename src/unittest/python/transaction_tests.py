from Crypto.Random import get_random_bytes
import sys
sys.path.append("../main/python")

from core.Transaction import Transaction
from unittest import TestCase
import datetime


class TransactionTest(TestCase):

    def test_setGetDate(self):
        trans = Transaction()
        date = datetime.datetime.now()
        trans.initializeCryptoEngine("password!", get_random_bytes(32))
        trans.setDate(date)

        self.assertFalse(trans._date == date)
        self.assertFalse(isinstance(trans._date, datetime.datetime))

        self.assertEquals(trans.getDate(), date)
        self.assertTrue(isinstance(trans.getDate(), datetime.datetime))

    def test_setGetDateWrongPassword(self):
        trans = Transaction()
        date = datetime.datetime.now()
        salt = get_random_bytes(32)
        trans.initializeCryptoEngine("password!", salt)
        trans.setDate(date)

        trans.initializeCryptoEngine("wrongone", salt)

        self.assertRaises(ValueError, trans.getDate)

    def test_setGetCurrency(self):
        trans = Transaction()
        trans.initializeCryptoEngine("password!", get_random_bytes(32))
        trans.setCurrency("EUR")

        self.assertFalse(trans._currency == "EUR")

        self.assertEquals(trans.getCurrency(), "EUR")

    def test_setGetAmountFloat(self):
        trans = Transaction()
        trans.initializeCryptoEngine("password!", get_random_bytes(32))
        trans.setAmount(100.0)

        self.assertFalse(trans._amount == 100.0)

        self.assertEquals(trans.getAmount(), 100.0)
        self.assertTrue(isinstance(trans.getAmount(), float))

    def test_setGetAmountString(self):
        trans = Transaction()
        trans.initializeCryptoEngine("password!", get_random_bytes(32))
        trans.setAmount("100.0")

        self.assertFalse(trans._amount == "100.0")

        self.assertEquals(trans.getAmount(), 100.0)
        self.assertTrue(isinstance(trans.getAmount(), float))

    def test_setGetAmountWrongPassword(self):
        trans = Transaction()
        salt = get_random_bytes(32)
        trans.initializeCryptoEngine("password!", salt)
        trans.setAmount(100.0)

        trans.initializeCryptoEngine("wrongone", salt)

        self.assertRaises(ValueError, trans.getAmount)

    def test_setGetCreditorName(self):
        trans = Transaction()
        trans.initializeCryptoEngine("password!", get_random_bytes(32))
        trans.setCreditorName("Creditor Name")

        self.assertFalse(trans._creditorName == "Creditor Name")

        self.assertEquals(trans.getCreditorName(), "Creditor Name")

    def test_setGetCreditorNameWrongPassword(self):
        trans = Transaction()
        salt = get_random_bytes(32)
        trans.initializeCryptoEngine("password!", salt)
        trans.setCreditorName("Creditor Name")

        trans.initializeCryptoEngine("wrongone", salt)
        self.assertRaises(ValueError, trans.getCreditorName)

    def test_setGetCreditorIban(self):
        trans = Transaction()
        trans.initializeCryptoEngine("password!", get_random_bytes(32))
        trans.setCreditorIban("Creditor Iban")

        self.assertFalse(trans._creditorIban == "Creditor Iban")

        self.assertEquals(trans.getCreditorIban(), "Creditor Iban")

    def test_setGetDebtorName(self):
        trans = Transaction()
        trans.initializeCryptoEngine("password!", get_random_bytes(32))
        trans.setDebtorName("Debtor Name")

        self.assertFalse(trans._debtorName == "Debtor Name")

        self.assertEquals(trans.getDebtorName(), "Debtor Name")

    def test_setGetDebtorIban(self):
        trans = Transaction()
        trans.initializeCryptoEngine("password!", get_random_bytes(32))
        trans.setDebtorIban("Debtor Iban")

        self.assertFalse(trans._debtorIban == "Debtor Iban")

        self.assertEquals(trans.getDebtorIban(), "Debtor Iban")
