from product import Product


class PhysicalProduct(Product):
    """A product that is stored and shipped."""

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        print("ID:", self.get_product_id(), "| Name:", self.get_name(),
              "| Price: $" + format(self.get_price(), ".2f"),
              "| Stock:", self.get_stock(),
              "| Weight:", self.__weight, "kg")
