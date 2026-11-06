import json
import os

from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from supplier import Supplier

FILENAME = "inventory.json"


DEFAULT_SUPPLIER = Supplier("S000", "Unknown Supplier", "none@example.com")


def create_supplier(data: dict) -> Supplier:
    return Supplier(data["supplier_id"], data["name"], data["contact_email"])


def create_product(item: dict) -> Product:
    supplier = create_supplier(item["supplier"]) if "supplier" in item else DEFAULT_SUPPLIER
    if item["type"] == "physical":
        return PhysicalProduct(item["id"], item["name"], item["price"],
                               item["stock"], supplier, item["weight"])
    if item["type"] == "digital":
        return DigitalProduct(item["id"], item["name"], item["price"],
                              item["stock"], supplier, item["download_size"])
    raise ValueError("unknown product type: " + str(item["type"]))


def load_inventory(inventory):
    if os.path.exists(FILENAME):
        print("inventory.json found.")
        file = open(FILENAME, "r")
        data = json.load(file)
        file.close()
        for item in data:
            inventory.add_product(create_product(item))
        print("Inventory loaded successfully.")
    else:
        print("inventory.json not found. Starting with empty inventory.")


def save_inventory(inventory):
    data = []
    for product in inventory.get_products():
        data.append(product.to_dict())
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
    print("1. Physical Product")
    print("2. Digital Product")
    product_type = input("Product type: ")

    if product_type not in ("1", "2"):
        print("Error: please choose 1 or 2.")
        return

    product_id = input("Product ID: ")

    if inventory.search_product(product_id) is not None:
        print("Error: that Product ID already exists.")
        return

    name = input("Product Name: ")
    supplier_id = input("Supplier ID: ")
    supplier_name = input("Supplier Name: ")
    supplier_email = input("Supplier Email: ")
    supplier = Supplier(supplier_id, supplier_name, supplier_email)

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        if product_type == "1":
            weight = float(input("Weight (kg): "))
        else:
            download_size = float(input("Download Size (MB): "))
    except ValueError:
        print("Error: invalid number entered.")
        return

    if price < 0 or stock < 0:
        print("Error: price and stock cannot be negative.")
        return

    if product_type == "1":
        if weight < 0:
            print("Error: weight cannot be negative.")
            return
        inventory.add_product(PhysicalProduct(product_id, name, price, stock, supplier, weight))
    else:
        if download_size < 0:
            print("Error: download size cannot be negative.")
            return
        inventory.add_product(DigitalProduct(product_id, name, price, stock, supplier, download_size))

    print("\nProduct added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    print("Name:", product.get_name())
    print("Current Stock:", product.get_stock())

    try:
        new_stock = int(input("\nNew Stock Quantity: "))
        product.update_stock(new_stock)
    except ValueError:
        print("Error: please enter a whole number of 0 or more.")
        return

    print("\nStock updated successfully!")


def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found")
    print("-" * 48)
    product.display_information()
    print(" ", product.get_fulfilment_info())
    product.display_supplier_information()
    print("-" * 48)


print("=" * 40)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 40)
print()

inventory = Inventory()
load_inventory(inventory)

while True:
    show_menu()
    option = input("\nEnter option: ")

    if option == "1":
        inventory.display_all()
    elif option == "2":
        add_product(inventory)
    elif option == "3":
        update_stock(inventory)
    elif option == "4":
        search_product(inventory)
    elif option == "5":
        print("\nSaving inventory...")
        save_inventory(inventory)
    elif option == "6":
        print("\nSaving inventory before exit...")
        save_inventory(inventory)
        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("Invalid option. Please choose 1-6.")
