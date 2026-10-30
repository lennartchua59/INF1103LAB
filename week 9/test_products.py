from physical_product import PhysicalProduct
from digital_product import DigitalProduct

print("--- 1.2 PhysicalProduct ---")
guitar = PhysicalProduct("P001", "Guitar", 450.0, 5, 3.5)
guitar.display_information()

print("--- 1.3 DigitalProduct ---")
os_product = DigitalProduct("D001", "Operating System", 99.0, 100, 4500)
os_product.display_information()
