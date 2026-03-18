class Product:
    """Represent a product with name, price, quantity, and active status."""
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Initialize a product with a name, price, and quantity."""
        if not name.strip():
            raise ValueError("Product name cannot be empty!")

        if price < 0:
            raise ValueError("Price cannot be negative!")

        if  quantity < 0:
            raise ValueError("Quantity cannot be negative!")

        self.name  = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Set the quantity of the product and update its active status.
        If the quantity is set to 0, the product becomes inactive.
        Otherwise, it becomes active.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative!")

        self.quantity = quantity

        if self.quantity == 0:
            self.active = False
        else:
            self.active = True

    def is_active(self) -> bool:
        """Return whether the product is active."""
        return self.active

    def activate(self) -> None:
        """Mark the product as active."""
        self.active = True

    def deactivate(self) -> None:
        """Mark the product as inactive."""
        self.active = False

    def show(self) -> None:
        """
        Print the product details in a readable format.
        Example:
        MacBook Air M2 | Price: 1450 | Quantity: 100 | Status: active
        """
        status = "active" if self.active else "inactive"
        print(f"{self.name} | Price: {self.price} | Quantity: {self.quantity} | Status: {status}")

    def buy(self, quantity: int) -> float:
        """
        Purchase a given quantity of the product.
        This reduces the available stock and returns the total price.
        If the stock reaches 0 after purchase, the product becomes inactive.
        Args:
         quantity (int): The number of units to buy.
        Returns:
         float: The total price for the purchased quantity.
        Raises:
         ValueError: If the product is inactive, the quantity is not greater
             than 0, or the requested quantity exceeds available stock.
        """
        if not self.active:
            raise ValueError(f"Product {self.name} is not available")

        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0!")

        if quantity > self.quantity:
            raise ValueError(f"Not enough stock. Available: {self.quantity}")

        total_price =  self.price * quantity

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return float(total_price)
