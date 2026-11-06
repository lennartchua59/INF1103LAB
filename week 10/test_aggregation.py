from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory


def check(description: str, condition: bool) -> None:
    print("PASS" if condition else "FAIL", "-", description)


print("--- Section 3: Aggregation (Inventory - Product) ---")
supplier = Supplier("S001", "Acme Supplies", "sales@acme.com")
mouse = PhysicalProduct("P002", "Mouse", 25.5, 60, supplier, 0.1)  # exists before any inventory
check("Product exists before being added to an Inventory", mouse.get_name() == "Mouse")

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(mouse)
check("Inventory A finds the product", inventory_a.find_product("P002") is mouse)

inventory_a.remove_product("P002")
check("Inventory A no longer holds the product", inventory_a.find_product("P002") is None)
check("find_product returns None for unknown id", inventory_a.find_product("X") is None)
print("Product still usable after removal:")
mouse.display_information()
mouse.update_stock(55)
check("Product still works (update_stock)", mouse.get_stock() == 55)

inventory_b.add_product(mouse)
check("Same Product object added to Inventory B", inventory_b.find_product("P002") is mouse)

inventory_b.remove_product("P002")
check("Emptied inventory does not destroy the product", mouse.get_name() == "Mouse")
