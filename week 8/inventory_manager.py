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


def save_inventory(inventory):
    data = []
    for product in inventory.get_products():
        data.append({"id": product.get_product_id(),
                     "name": product.get_name(),
                     "price": product.get_price(),
                     "stock": product.get_stock()})
    file = open(FILENAME, "w")
    json.dump(data, file, indent=4)
    file.close()
    print("Inventory saved successfully to inventory.json.")


def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")

    if inventory.search_product(product_id) is not None:
        print("Error: that Product ID already exists.")
        return

    name = input("Product Name: ")

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Error: invalid price or stock quantity.")
        return

    if price < 0 or stock < 0:
        print("Error: price and stock cannot be negative.")
        return

    inventory.add_product(Product(product_id, name, price, stock))
    print("\nProduct added successfully!")
