from product import Product
from order_line import OrderLine


class Order:
    """Composition: an Order creates and manages its own OrderLine objects."""

    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def get_order_id(self) -> str:
        return self.__order_id

    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        # The line is created here, never passed in from outside.
        self.__order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, product_id: str) -> None:
        for line in self.__order_lines:
            if line.get_product().get_product_id() == product_id:
                self.__order_lines.remove(line)
                return

    def calculate_total(self) -> float:
        total: float = 0.0
        for line in self.__order_lines:
            total += line.calculate_subtotal()
        return total

    def display_information(self) -> None:
        print("Order", self.__order_id)
        for line in self.__order_lines:
            print("  ", end="")
            line.display_information()
        print("  Total: $" + format(self.calculate_total(), ".2f"))
