from app.DTO.BookDTO import BookDTO
from app.Models.Book import Book

class BookMapper:
    @staticmethod
    def to_dto(book: Book) -> BookDTO:
        return BookDTO(
            id=book.id, 
            name=book.name,
            author_id=book.author_id,
            publisher_id=book.publisher_id,
            available_copies_in_library=book.available_copies_in_library,
            available_copies_for_sale=book.available_copies_for_sale,
            price=book.price,
            location=book.location,
            created_at=book.created_at,
            updated_at=book.updated_at
        )

    @staticmethod
    def from_dto(book_dto: BookDTO) -> Book:
        return Book(id=book_dto.id, name=book_dto.name, author=book_dto.author)
