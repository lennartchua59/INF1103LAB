from product import Product


class DigitalProduct(Product):
    """A product that is delivered as a download."""

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print("    Download Size:", self.__download_size, "MB")
