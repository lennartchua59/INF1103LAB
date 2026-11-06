from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


def check(description: str, condition: bool) -> None:
    print("PASS" if condition else "FAIL", "-", description)


def show_product_details(product: Product) -> None:
    """Works for ANY Product; never asks which subclass it is (LSP)."""
    product.display_information()
    print(product.get_fulfilment_info())


supplier = Supplier("S001", "Acme Supplies", "sales@acme.com")
guitar = PhysicalProduct("P001", "Guitar", 450.0, 8, supplier, 3.5)
software = DigitalProduct("D001", "Operating System", 99.0, 100, supplier, 4500.0)

print("--- Section 6: LSP - same function, both subclasses ---")
show_product_details(guitar)
show_product_details(software)

print("\n--- LSP: update_stock keeps the same meaning in both subclasses ---")
for item in (guitar, software):
    item.update_stock(42)
    check(item.get_name() + " update_stock(42) -> stock is 42", item.get_stock() == 42)
    try:
        item.update_stock(-1)
        check(item.get_name() + " rejects negative stock", False)
    except ValueError:
        check(item.get_name() + " rejects negative stock", True)

print("\n--- Section 7: Polymorphism through one Product collection ---")
inventory = Inventory()
inventory.add_product(guitar)
inventory.add_product(software)
check("both types stored in the same Inventory", len(inventory.get_products()) == 2)

outputs: list[str] = []
for product in inventory.get_products():     # no isinstance(), one loop
    product.display_information()
    info = product.get_fulfilment_info()
    print(info)
    outputs.append(info)
check("physical fulfilment mentions shipping", "shipping" in outputs[0])
check("digital fulfilment mentions download", "download" in outputs[1])
inventory.display_all_products()
