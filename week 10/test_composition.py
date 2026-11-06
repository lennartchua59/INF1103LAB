from supplier import Supplier
from physical_product import PhysicalProduct
from dockertest import DigitalProduct
from order import Order


def check(description: str, condition: bool) -> None:
    print("PASS" if condition else "FAIL", "-", description)


print("--- Section 4: Composition (Order - OrderLine) ---")
supplier = Supplier("S001", "Acme Supplies", "sales@acme.com")
guitar = PhysicalProduct("P001", "Guitar", 450.0, 8, supplier, 3.5)
software = DigitalProduct("D001", "Operating System", 99.0, 100, supplier, 4500.0)

order1 = Order("O1")
order1.add_order_line(guitar, 2)
order1.add_order_line(software, 3)
order1.display_information()
check("total = 2*450 + 3*99 = 1197.00", abs(order1.calculate_total() - 1197.0) < 0.001)

order2 = Order("O2")
order2.add_order_line(guitar, 1)
order2.display_information()

line1 = order1.get_order_lines()[0]
line2 = order2.get_order_lines()[0]
# Predict first: same Product in two Orders -> 2 OrderLines, 1 Product.
check("two different OrderLine objects", line1 is not line2)
check("one shared Product object", line1.get_product() is line2.get_product())
print("id(line1) =", id(line1), "| id(line2) =", id(line2))
print("id(product in line1) =", id(line1.get_product()), "| id(product in line2) =", id(line2.get_product()))

order1.remove_order_line("D001")
check("order line removed through the Order", len(order1.get_order_lines()) == 1)
check("removing the line does not destroy the Product", software.get_name() == "Operating System")
check("OrderLine of order 2 unaffected", len(order2.get_order_lines()) == 1)
