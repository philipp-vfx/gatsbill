from core.DBUtils import Helper
from core.User import User
from core.Transaction import Transaction

class Main:
    """
    Main Class
    """

    def main(self):
        """
        Main method. Starting point for every code execution.
        """
        #DB TEST
        dbhelper = Helper.instance()
        dbhelper.setDbPath("D:\\Python\\Buchhaltungssoftware\\db_test\\test.db")
        engine = dbhelper.getEngine()
        base = dbhelper.getOrmBase()
        base.metadata.create_all(engine)
        user = User("testuser", "max", "mustermann", "password")
        transaction = Transaction()
        transaction.initializeCryptoEngine("password", user.getSalt())
        transaction.setCurrency("EUR")
        transaction.setAmount(1000)
        transaction.setDescription("Test Transaction")
        user.addTransaction(transaction)
        session = dbhelper.getSession()
        session.add(user)
        session.commit()
        dbhelper.closeSession()


if __name__ == "__main__":
    main = Main()
    main.main()
