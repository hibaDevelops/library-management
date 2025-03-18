class SaleBookDTO:
    def __init__(
        self,
        id: int,
        name: str,
        price: float,
        quantity: int,
    ):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price,
        }

    def __repr__(self):
        return f"SaleBookDTO(id={self.id}, name='{self.name}'')"
