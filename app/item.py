from os import environ

import mysql.connector
from dotenv import load_dotenv

load_dotenv('./.env.local')

USERNAME = environ.get('DB_USER')
PASSWORD = environ.get('DB_PASSWORD')
HOST = environ.get('DB_HOST')
DATABASE_NAME = environ.get('DB_NAME')


class DB:

    def get_db_conn(self):
        try:
            return mysql.connector.connect(
                host=HOST, user=USERNAME, password=PASSWORD,
                database=DATABASE_NAME, buffered=True)

        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return

    def get_cursor(self, db_conn):
        try:
            return db_conn.cursor()
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return


class Item:
    """ id, title, isbn, quantity """

    def __init__(self):
        db = DB()
        self.db_conn = db.get_db_conn()
        self.cur = db.get_cursor(self.db_conn)

    def create(self, title, quantity=1):
        isbn = self.generate_isbn()

        sql_query = "INSERT INTO `item`(title`, `isbn`, `quantity`) VALUES (%s, %s, %s);"
        values = (title, isbn, quantity)

        self.cur.execute(sql_query, values)

        if not self.cur:
            return False

        self.db_conn.commit()
        self.db_conn.close()

        return True

    def select_all(self):
        items = []

        sql_query = "SELECT `id`, `title`, `isbn`, `quantity`, `add_at`, `update_at` FROM `item`;"

        self.cur.execute(sql_query)

        if not self.cur:
            return False

        items = self.cur.fetchall()

        self.db_conn.close()

        return items

    def select_one(self, item_key, item_value):
        sql_query = f"SELECT `id`, `title`, `isbn`, `quantity`, `add_at`, `update_at` FROM `item` WHERE `{item_key}`=%s;"

        try:
            self.cur.execute(sql_query, (item_value, ))
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return False

        if not self.cur:
            return False

        item = self.cur.fetchone()

        self.db_conn.close()

        return item

    def update(self):
        pass

    def delete(self):
        pass

    @staticmethod
    def generate_id():
        pass

    @classmethod
    def scan_data_title(cls, title):
        pass

    @classmethod
    def scan_data_isbn(cls, isbn):
        pass
