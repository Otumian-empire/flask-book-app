# Assuming this is a valid databse model
from .item import Item

def create_item(*, item_name, item_quantity=1):
    item = Item(item_name, item_quantity)
    item.save()
    pass
    
def read_item_by_name(*, item_name):
    pass
    
def read_item_by_quantity(*, item_quantity):
    pass
    
def read_items():
    pass
    
def update():
    pass
    
def delete():
    pass
    


