from product import Product


class OrderLine:
    """Part of an Order (composition). Created only by Order.add_order_line()."""

    def __init__(self, product: Product, quantity: int) -> None:
        self.__product: Product = product  # association: the line does not own the Product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> None:
        print(self.__product.get_name(), "x", self.__quantity,
              "= $" + format(self.calculate_subtotal(), ".2f"))
