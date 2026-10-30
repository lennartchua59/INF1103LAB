class Inventory:
    """Manages a collection of Product objects."""

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def get_products(self):
        return list(self.__products)

    def display_all(self):
        print("\nCurrent Inventory")
        print("-" * 48)
        for product in self.__products:
            product.display_information()
        print("-" * 48)
