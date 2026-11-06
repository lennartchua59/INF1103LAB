from product import Product


class Inventory:
    """Aggregation: an Inventory holds Product references but does not own them."""

    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> None:
        # Only the reference is removed; the Product object itself lives on.
        product = self.find_product(product_id)
        if product is not None:
            self.__products.remove(product)

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def get_products(self) -> list[Product]:
        return list(self.__products)

    def display_all_products(self) -> None:
        for product in self.__products:
            product.display_information()

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        print("-" * 48)
        self.display_all_products()
        print("-" * 48)
