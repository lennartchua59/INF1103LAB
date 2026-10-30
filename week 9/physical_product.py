from product import Product
from can_be_shipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    """A product that is stored and shipped."""

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print("    Weight:", self.__weight, "kg")

    def get_fulfilment_info(self):
        return "Requires physical shipping to the customer."

    def calculate_shipping_cost(self):
        # simple rule: $5.00 base fee plus $2.00 per kilogram
        return 5.0 + 2.0 * self.__weight
