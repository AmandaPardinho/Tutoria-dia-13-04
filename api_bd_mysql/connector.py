import mysql.connector
class DBConnector:
    # Define o objeto dbconnector
    def __init__(self, host, user, password, database):
        self.host = host,
        self.user = user,
        self.password = password,
        self.database = database
        self.connection = None,
        self.cursor = None

    # Cria a conexão
    def connect(self):
        self.connection = mysql.connector.connect(
        host = self.host,
        user = self.user,
        password = self.password,
        database = self.ecommerce
    )
        self.cursor = self.connection.cursor()
