from app.DTO.AuthorDTO import AuthorDTO
from app.DTO.BookDTO import BookDTO
from app.DTO.PublisherDTO import PublisherDTO
from app.Models.Book import Book


class BookMapper:
    @staticmethod
    def to_dto(book: Book, author: AuthorDTO or None, publisher: PublisherDTO or None) -> BookDTO:
        return BookDTO(
            id=book.id,
            name=book.name,
            available_copies_in_library=book.available_copies_in_library,
            available_copies_for_sale=book.available_copies_for_sale,
            price=book.price,
            location=book.location,
            created_at=book.created_at,
            updated_at=book.updated_at,
            author=author,
            publisher=publisher
        )

    @staticmethod
    def from_dto(book_dto: BookDTO) -> Book:
        return Book(id=book_dto.id, name=book_dto.name, author=book_dto.author)
