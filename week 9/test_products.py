import io
from contextlib import redirect_stdout

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product import Product
from can_be_shipped import CanBeShipped


def capture(product):
    """Run display_information() and return what it printed."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        product.display_information()
    return buffer.getvalue()


def check(description, condition):
    print("PASS" if condition else "FAIL", "-", description)


print("--- 1.2 PhysicalProduct ---")
guitar = PhysicalProduct("P001", "Guitar", 450.0, 5, 3.5)
guitar.display_information()

print("--- 1.3 DigitalProduct ---")
os_product = DigitalProduct("D001", "Operating System", 99.0, 100, 4500)
os_product.display_information()

print("--- 2.2 Overriding output ---")
physical_output = capture(guitar)
digital_output = capture(os_product)
check("physical shows common info from Product", "ID: P001" in physical_output and "$450.00" in physical_output)
check("physical shows its own weight", "Weight: 3.5 kg" in physical_output)
check("digital shows common info from Product", "ID: D001" in digital_output and "$99.00" in digital_output)
check("digital shows its own download size", "Download Size: 4500 MB" in digital_output)

print("--- 3.2 get_fulfilment_info() ---")
print("Physical:", guitar.get_fulfilment_info())
print("Digital:", os_product.get_fulfilment_info())
check("physical fulfilment mentions shipping", "shipping" in guitar.get_fulfilment_info())
check("digital fulfilment mentions digitally", "digitally" in os_product.get_fulfilment_info())

print("--- 3.3 Abstract Product cannot be instantiated ---")
try:
    Product("X001", "Generic", 10.0, 1)
    check("Product() raises TypeError", False)
except TypeError as error:
    print("TypeError:", error)
    check("Product() raises TypeError", True)

print("--- 4.2 CanBeShipped ---")
light = PhysicalProduct("P002", "Mouse", 25.5, 60, 0.1)
heavy = PhysicalProduct("P003", "Monitor", 299.99, 10, 6.0)
for item in (light, guitar, heavy):
    print(item.get_name(), "(" + str(item.get_weight()) + " kg) ships for $" + format(item.calculate_shipping_cost(), ".2f"))
check("0.1 kg costs $5.20", abs(light.calculate_shipping_cost() - 5.2) < 0.001)
check("3.5 kg costs $12.00", abs(guitar.calculate_shipping_cost() - 12.0) < 0.001)
check("6.0 kg costs $17.00", abs(heavy.calculate_shipping_cost() - 17.0) < 0.001)
check("PhysicalProduct is a CanBeShipped", isinstance(guitar, CanBeShipped))
check("DigitalProduct is not a CanBeShipped", not isinstance(os_product, CanBeShipped))

print("--- 7. Inventory operations and JSON data ---")
from inventory import Inventory

inventory = Inventory()
inventory.add_product(guitar)
inventory.add_product(os_product)
check("inventory holds both product types", len(inventory.get_products()) == 2)
check("search finds a physical product", inventory.search_product("P001") is guitar)
check("search finds a digital product", inventory.search_product("D001") is os_product)
check("search returns None for unknown ID", inventory.search_product("P999") is None)
guitar.update_stock(8)
check("update_stock changes the stock", guitar.get_stock() == 8)
inventory.display_all()
check("physical to_dict has type and weight", guitar.to_dict()["type"] == "physical" and guitar.to_dict()["weight"] == 3.5)
check("digital to_dict has type and download_size", os_product.to_dict()["type"] == "digital" and os_product.to_dict()["download_size"] == 4500)
