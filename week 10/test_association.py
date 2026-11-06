from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


def check(description: str, condition: bool) -> None:
    print("PASS" if condition else "FAIL", "-", description)


print("--- Section 2: Association (Supplier - Product) ---")
supplier = Supplier("S001", "Acme Supplies", "sales@acme.com")
guitar = PhysicalProduct("P001", "Guitar", 450.0, 8, supplier, 3.5)
software = DigitalProduct("D001", "Operating System", 99.0, 100, supplier, 4500.0)

print("Supplier info through the physical product:")
guitar.display_supplier_information()
print("Supplier info through the digital product:")
software.display_supplier_information()

check("both products reference the same Supplier object",
      guitar.get_supplier() is supplier and software.get_supplier() is supplier)
check("Supplier and Product are separate objects", supplier is not guitar)

# Predict first: delete the supplier variable.
del supplier
print("After 'del supplier':")
guitar.display_supplier_information()
software.display_supplier_information()
check("product still shows supplier info after del supplier",
      guitar.get_supplier().get_name() == "Acme Supplies")
