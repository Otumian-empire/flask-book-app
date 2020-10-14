import mysql.connector

class Item:
    """ id, title, isbn, quantity """
    def create(self, title, quantity=1):
        self.title = title
        self.quantity = quantity
        self.isbn = self.generate_isbn()

    def save(self):
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
