import json
import os

from product import Product
from inventory import Inventory

FILENAME = "inventory.json"


def load_inventory(inventory):
    if os.path.exists(FILENAME):
        print("inventory.json found.")
        file = open(FILENAME, "r")
        data = json.load(file)
        file.close()
        for item in data:
            inventory.add_product(
                Product(item["id"], item["name"], item["price"], item["stock"]))
        print("Inventory loaded successfully.")
    else:
        print("inventory.json not found. Starting with empty inventory.")
