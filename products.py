class Product:
    """Represent a product with name, price, quantity, and active status."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Initialize a product with a name, price, and quantity."""
        if not name.strip():
            raise ValueError("Product name cannot be empty!")

        if price < 0:
            raise ValueError("Price cannot be negative!")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative!")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self) -> int:
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """Set the quantity and update active status."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative!")

        self.quantity = quantity
        self.active = self.quantity != 0

    def is_active(self) -> bool:
        """Return whether the product is active."""
        return self.active

    def activate(self) -> None:
        """Mark the product as active."""
        self.active = True

    def deactivate(self) -> None:
        """Mark the product as inactive."""
        self.active = False

    def set_promotion(self, promotion) -> None:
        """Set a promotion for the product."""
        self.promotion = promotion

    def get_promotion(self):
        """Return the current promotion of the product."""
        return self.promotion

    def show(self) -> None:
        """Print the product details in a readable format."""
        status = "active" if self.active else "inactive"

        if self.promotion is not None:
            print(
                f"{self.name} | Price: {self.price} | Quantity: {self.quantity} "
                f"| Promotion: {self.promotion.name} | Status: {status}"
            )
        else:
            print(
                f"{self.name} | Price: {self.price} | Quantity: {self.quantity} "
                f"| Status: {status}"
            )

    def buy(self, quantity: int) -> float:
        """Purchase a given quantity and return total price."""
        if not self.active:
            raise ValueError(f"Product {self.name} is not available")

        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0!")

        if quantity > self.quantity:
            raise ValueError(f"Not enough stock. Available: {self.quantity}")

        if self.promotion is not None:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return float(total_price)


class NonStockedProduct(Product):
    """Represent a product with unlimited stock."""

    def __init__(self, name: str, price: float):
        super().__init__(name, price, 0)
        self.active = True

    def show(self) -> None:
        """Print the non-stocked product details."""
        status = "active" if self.active else "inactive"

        if self.promotion is not None:
            print(
                f"{self.name} | Price: {self.price} | Quantity: Non-stocked "
                f"| Promotion: {self.promotion.name} | Status: {status}"
            )
        else:
            print(
                f"{self.name} | Price: {self.price} | Quantity: Non-stocked "
                f"| Status: {status}"
            )

    def buy(self, quantity: int) -> float:
        """Purchase a non-stocked product."""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0!")

        if self.promotion is not None:
            return float(self.promotion.apply_promotion(self, quantity))

        return float(self.price * quantity)


class LimitedProduct(Product):
    """Represent a product with a maximum amount per order."""

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)

        if maximum <= 0:
            raise ValueError("Maximum must be greater than 0!")

        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """Purchase a limited product."""
        if quantity > self.maximum:
            raise ValueError("You cannot buy more than the allowed limit.")
        return super().buy(quantity)

    def show(self) -> None:
        """Print the limited product details."""
        status = "active" if self.active else "inactive"

        if self.promotion is not None:
            print(
                f"{self.name} | Price: {self.price} | Quantity: {self.quantity} "
                f"| Max per order: {self.maximum} | Promotion: {self.promotion.name} "
                f"| Status: {status}"
            )
        else:
            print(
                f"{self.name} | Price: {self.price} | Quantity: {self.quantity} "
                f"| Max per order: {self.maximum} | Status: {status}"
            )
