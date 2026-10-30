from abc import ABC, abstractmethod


class Product(ABC):
    """Abstract base class for every product (physical or digital)."""

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        if quantity < 0:
            raise ValueError("stock cannot be negative")
        self.__stock = quantity

    def display_information(self):
        print("ID:", self.__product_id, "| Name:", self.__name,
              "| Price: $" + format(self.__price, ".2f"),
              "| Stock:", self.__stock)

    @abstractmethod
    def get_fulfilment_info(self):
        """Describe how this product is delivered to the customer."""
        pass
