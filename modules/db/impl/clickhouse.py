from ..database import Database
from clickhouse_driver import Client

class ClickhosueDriver(Database):
    def __init__(self, address, port, username, password):
        self.address = address
        self.port = port
        self.username = username
        self.password = password

        self.client = None

    def table_exists(self, table):
        
    
    def connect(self):
        self.client = Client(host = self.address, port = self.port, user = self.username, password = self.password)

    def add(self, table, key, value):
