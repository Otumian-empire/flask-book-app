from os import environ
from uuid import uuid4

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
    """
    id, title, isbn, quantity

    use uuid4 in place of isbn but let property rename
    """

    def __init__(self):
        db = DB()
        self.db_conn = db.get_db_conn()
        self.cur = db.get_cursor(self.db_conn)

    def create(self, title, quantity=1):
        isbn = str(self.generate_isbn())

        sql_query = "INSERT INTO `item`(`title`, `isbn`, `quantity`) VALUES (%s, %s, %s);"
        values = (title.lower(), isbn, quantity)

        try:
            self.cur.execute(sql_query, values)
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return False

        if not self.cur:
            return False

        self.db_conn.commit()
        self.db_conn.close()

        return True

    def select_all(self):
        items = []

        sql_query = "SELECT `id`, `title`, `isbn`, `quantity`, `add_at`, `update_at` FROM `item`;"

        try:
            self.cur.execute(sql_query)
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return items

        if not self.cur:
            return items

        items = self.cur.fetchall()

        self.db_conn.close()

        return items

    def select_one(self, item):
        item_key, item_value = list(item.items())[0]

        sql_query = f"SELECT `id`, `title`, `isbn`, `quantity`, `add_at`, `update_at` FROM `item` WHERE `{item_key}`=%s;"
        values = (str(item_value).lower(), )

        try:
            self.cur.execute(sql_query, values)
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return []

        if not self.cur:
            return []

        item = self.cur.fetchone()

        self.db_conn.close()

        return item

    def update(self, item, where_clause):
        # `{item_key}`=%s,
        set_body_keys = ""

        for set_item in item.items():
            set_body_keys += f"`{set_item[0]}`=%s,"

        set_item_values = tuple([str(set_item[1]).lower()
                                 for set_item in item.items()])

        where_clause_key, where_clause_value = list(where_clause.items())[0]

        values = set_item_values + (str(where_clause_value).lower(),)

        sql_query = f"UPDATE `item` SET {set_body_keys} `update_at`=CURRENT_TIMESTAMP WHERE `{where_clause_key}`=%s;"

        try:
            self.cur.execute(sql_query, values)
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return False

        if not self.cur:
            return False

        self.db_conn.commit()
        self.db_conn.close()

        return True

    def delete(self, item):
        item_key, item_value = list(item.items())[0]

        sql_query = f"DELETE FROM `item` WHERE `{item_key}`=%s;"
        values = (str(item_value).lower(), )

        try:
            self.cur.execute(sql_query, values)
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return False

        if not self.cur:
            return False

        self.db_conn.commit()
        self.db_conn.close()

        return True

    @staticmethod
    def generate_isbn():
        return uuid4()


# i = Item()

# print(i.create('24pill-code'))
# print(i.select_all())
# print(i.select_one({'title':'24pill-code'}))
# print(i.update({'title':'24pill-code-book'}, {'title':'24pill-code'}))
# print(i.delete({'title':'24pill-code-book'}))
