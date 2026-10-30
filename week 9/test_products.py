import io
from contextlib import redirect_stdout

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product import Product


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
