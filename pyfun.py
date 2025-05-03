class Product:
    """Represents a product with name, price, and quantity."""

    def __init__(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_inventory(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.quantity += amount

    def remove_inventory(self, amount):
        if amount < 0 or amount > self.quantity:
            raise ValueError("Invalid amount to remove.")
        self.quantity -= amount

    def total_value(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"{self.name}: ${self.price:.2f}, Qty: {self.quantity}, Total: ${self.total_value():.2f}")


# Example usage
p = Product("Pen", 1.5, 50)
p.display_info()
p.add_inventory(10)
p.remove_inventory(5)
p.display_info()
