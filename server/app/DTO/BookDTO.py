class BookDTO:
    def __init__(
        self, id: int, 
        name: str, 
        author_id: int, 
        publisher_id: int,
        available_copies_in_library: int,
        available_copies_for_sale: int,
        price: float,
        location: str,
        created_at: str,
        updated_at: str
        ):
            self.id = id
            self.name = name
            self.author_id = author_id
            self.publisher_id = publisher_id
            self.available_copies_in_library = available_copies_in_library
            self.available_copies_for_sale = available_copies_for_sale
            self.price = price
            self.location = location
            self.created_at = created_at
            self.updated_at = updated_at

    @classmethod
    def from_model(cls, book):
        return cls(id=book.id, name=book.name)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'author_id': self.author_id,
            'publisher_id': self.publisher_id,
            'available_copies_in_library': self.available_copies_in_library,
            'available_copies_for_sale': self.available_copies_for_sale,
            'price': self.price,
            'location': self.location,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    def __repr__(self):
        return f"BookDTO(id={self.id}, name='{self.name}'')"
