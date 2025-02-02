class BookDTO:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @classmethod
    def from_model(cls, book):
        return cls(id=book.id, name=book.name)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def __repr__(self):
        return f"BookDTO(id={self.id}, name='{self.name}'')"
