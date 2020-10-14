# Assuming this is a valid databse model
from .item import Item

# TODO: Implement corresponding component in `item.py`


def create_item(*, item_name, item_quantity=1):
    item = Item()
    return item.create(item_name, item_quantity)


# TODO: create at least one item at a code, max is 10
def create_many_items(*, items):
    pass


def read_one_item(*, item_key, item_value):
    item = Item()
    return item.select_one(item_key, item_value)


def read_all_items(self):
    item = Item()
    return item.select_all()


def update():
    pass


# TODO: update at least one item at a code, max is 10
def update_many():
    pass


def delete():
    pass


# TODO: update at least one item at a code, max is 10
def delete_many():
    pass
