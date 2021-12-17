from unittest import TestCase
import sys
sys.path.append("../main/python")
from core.User import User

class UserTest(TestCase):

    def test_verifyPasswordCorrect(self):
        user = User("username", "Max", "Mustermann", "password1234")

        self.assertFalse(user._passwordHash == "password1234")
        self.assertTrue(user.verifyPassword("password1234"))

    def test_verifyPasswordIncorrect(self):
        user = User("username", "Max", "Mustermann", "password1234")

        self.assertFalse(user.verifyPassword("falschePwd"))

    def test_getFirstname(self):
        user = User("username", "Max", "Mustermann", "password1234")

        self.assertFalse(user._firstName == "Max")
        self.assertEquals(user.getFirstName(), "Max")

    def test_getLastname(self):
        user = User("username", "Max", "Mustermann", "password1234")

        self.assertFalse(user._lastName == "Mustermann")
        self.assertEquals(user.getLastName(), "Mustermann")

    def test_setFirstName(self):
        user = User("username", "Max", "Mustermann", "password1234")
        user.setFirstName("Bob")
        self.assertFalse(user._firstName == "Bob")
        self.assertEquals(user.getFirstName(), "Bob")

    def test_setLastName(self):
        user = User("username", "Max", "Mustermann", "password1234")
        user.setLastName("Meier")
        self.assertFalse(user._lastName == "Meier")
        self.assertEquals(user.getLastName(), "Meier")

    def test_setPasswordCorrect(self):
        user = User("username", "Max", "Mustermann", "password1234")
        user.setPassword("password1234")
        self.assertEquals(user._password, "password1234")

    def test_setPasswordIncorrect(self):
        user = User("username", "Max", "Mustermann", "password1234")
        self.assertRaises(ValueError, user.setPassword, "wrongpwd")
