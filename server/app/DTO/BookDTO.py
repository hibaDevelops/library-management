from typing import Optional

from app.DTO.AuthorDTO import AuthorDTO
from app.DTO.PublisherDTO import PublisherDTO


class BookDTO:
    def __init__(
        self, id: int,
        name: str,
        available_copies_in_library: int,
        available_copies_for_sale: int,
        price: float,
        location: str,
        language: str,
        photo: str,
        created_at: str,
        updated_at: str,
        author: Optional[AuthorDTO] = None,
        publisher: Optional[PublisherDTO] = None,
    ):
        self.id = id
        self.name = name
        self.available_copies_in_library = available_copies_in_library
        self.available_copies_for_sale = available_copies_for_sale
        self.price = price
        self.location = location
        self.language = language
        self.photo = photo
        self.created_at = created_at
        self.updated_at = updated_at
        if author is None:
            self.author = None  # Handle None case or provide default behavior
        else:
            self.author = author
        if publisher is None:
            self.publisher = None  # Handle None case or provide default behavior
        else:
            self.publisher = publisher

    @classmethod
    def from_model(cls, book):
        return cls(id=book.id, name=book.name)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'available_copies_in_library': self.available_copies_in_library,
            'available_copies_for_sale': self.available_copies_for_sale,
            'price': self.price,
            'location': self.location,
            'language': self.language,
            'photo': self.photo,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'author': self.author,
            'publisher': self.publisher
        }

    def __repr__(self):
        return f"BookDTO(id={self.id}, name='{self.name}'')"
