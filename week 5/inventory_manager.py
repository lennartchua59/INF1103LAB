import json
import os

FILENAME = "inventory.json"


def display_all(inventory):
    print("\nCurrent Inventory")
    print("-" * 48)
    for product in inventory:
        print("ID:", product["id"], "| Name:", product["name"],
              "| Price: $" + format(product["price"], ".2f"),
              "| Stock:", product["stock"])
    print("-" * 48)


def find_product(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None


def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")

    if find_product(inventory, product_id) is not None:
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

    product = {"id": product_id, "name": name, "price": price, "stock": stock}
    inventory.append(product)
    print("\nProduct added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    product = find_product(inventory, product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    print("Name:", product["name"])
    print("Current Stock:", product["stock"])

    try:
        new_stock = int(input("\nNew Stock Quantity: "))
    except ValueError:
        print("Error: please enter a whole number.")
        return

    if new_stock < 0:
        print("Error: stock cannot be negative.")
        return

    product["stock"] = new_stock
    print("\nStock updated successfully!")


def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = find_product(inventory, product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found")
    print("-" * 48)
    print("ID:", product["id"])
    print("Name:", product["name"])
    print("Price: $" + format(product["price"], ".2f"))
    print("Stock:", product["stock"])
    print("-" * 48)


def load_inventory():
    if os.path.exists(FILENAME):
        print("inventory.json found.")
        file = open(FILENAME, "r")
        inventory = json.load(file)
        file.close()
        print("Inventory loaded successfully.")
        return inventory

    print("inventory.json not found. Starting with empty inventory.")
    return []


inventory = load_inventory()
display_all(inventory)
