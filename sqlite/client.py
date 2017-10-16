from sqlite3 import *

class SQLiteClient(object):
    """Connect to a SQLite database and perform CRUD operations."""

    # Open connection:
    def connect(self):
        self.conn = connect('orders.db')
        self.c = self.conn.cursor()

    # Create table:
    def createTable(self):
        if (self.c != None):
            self.c.execute('''CREATE TABLE IF NOT EXISTS OrderHeader
                     (OrderNum INTEGER, LineNum INTEGER, Price REAL, Qty REAL, Comment TEXT)''')

    # Drop table:
    def dropTable(self):
        if (self.c != None):
            self.c.execute("DROP TABLE IF EXISTS OrderHeader")

    # Insert a row of data:
    def insertData(self):
        if (self.c != None):
            self.c.execute("INSERT INTO OrderHeader VALUES (1205, 1, 25.44, 35, 'HOT RUSH')")
            self.c.execute("INSERT INTO OrderHeader VALUES (1206, 2, 16.32, 55, 'HOT HOT RUSH')")
            self.c.execute("INSERT INTO OrderHeader VALUES (1207, 3, 20.11, 42, 'HOTTER RUSH')")
            self.c.execute("INSERT INTO OrderHeader VALUES (1208, 4, 21.73, 44, 'SUPER HOT RUSH')")

    # Get all rows:
    def readAll(self):
        if (self.c != None):
            self.c.execute("SELECT * FROM OrderHeader")

    # Commit transaction:
    def commit(self):
        if (self.conn != None):
            self.conn.commit()

    # Rollback transaction:
    def rollback(self):
        if (self.conn != None):
            self.conn.rollback()

    # Close connection:
    def close(self):
        if (self.conn != None):
            self.conn.close()

