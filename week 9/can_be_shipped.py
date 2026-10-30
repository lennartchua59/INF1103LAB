from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    """Interface for any object that can be shipped."""

    @abstractmethod
    def calculate_shipping_cost(self):
        """Return the cost of shipping this object."""
        pass
