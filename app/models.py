# Assuming this is a valid databse model
from .item import Item


def create_item(*, item_name, item_quantity=1):

    if int(float(item_quantity)) < 1:
        item_quantity = 1

    item_ = Item()
    return item_.create(item_name, item_quantity)


def read_one_item(*, item):
    item_ = Item()
    return item_.select_one(item)


def read_all_items():
    item_ = Item()
    return item_.select_all()


def update(*, item, where_clause):
    item_ = Item()
    return item_.update(item, where_clause)


def delete(*, item):
    item_ = Item()
    return item_.delete(item)

# print(create_item(item_name='24pill-code', item_quantity=100))
# print(read_all_items())
# print(read_one_item(item={'title': '24pill-code'}))
# print(update(
#     item={'title': '24pill-code-book'},
#     where_clause={'title': '24pill-code'}))
# print(delete(item={'title': '24pill-code-book'}))


# TODO: Implement corresponding component in `item.py`


# TODO: create at least one item at a code, max is 10
def create_many_items(*, items):
    pass


# TODO: update at least one item at a code, max is 10
def update_many():
    pass


# TODO: update at least one item at a code, max is 10
def delete_many():
    pass
