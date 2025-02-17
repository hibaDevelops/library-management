class LendingBookDTO:
    def __init__(
        self,
        id: int,
        name: str,
    ):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return f"LendingBookDTO(id={self.id}, name='{self.name}'')"
