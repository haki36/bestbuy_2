from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass

class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        total_price = product.price * quantity
        discount = total_price * (self.percent / 100)
        return total_price - discount

class SecondItemHalfPrice(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2

        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)

class Buy2Get1Free(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        free_items = quantity // 3
        paid_items = quantity - free_items

        return paid_items * product.price
