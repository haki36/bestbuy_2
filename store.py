class Store:
    """Represent a store that manages a collection of products."""

    def __init__(self, product_list=None):
        """Initialize the store with an optional list of products."""
        if product_list is not None:
            self.product_list = product_list
        else:
            self.product_list = []

    def add_product(self, product):
        """Add a product to the store."""
        self.product_list.append(product)

    def remove_product(self, product):
        """Remove a product from the store if it exists."""
        if product in self.product_list:
            self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total quantity of all products in the store."""
        total = 0
        for product in self.product_list:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> list:
        """Return a list of all active products in the store."""
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        """
        Process an order for the given shopping list.
        Each item in the shopping list must be a tuple containing a product
        and the quantity to buy.
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            if product not in self.product_list:
                raise ValueError(f"Product {product.name} is not in the store.")

            if not product.is_active():
                raise ValueError(f"Product {product.name} is not available.")

            if quantity <= 0:
                raise ValueError("Purchase quantity must be greater than 0!")

            if quantity > product.get_quantity():
                raise ValueError(
                    f"Not enough stock for {product.name}. Available: {product.get_quantity()}"
                )

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price