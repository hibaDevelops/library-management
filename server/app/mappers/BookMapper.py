from app.DTO.BookDTO import BookDTO
from app.Models.Book import Book

class BookMapper:
    @staticmethod
    def to_dto(book: Book) -> BookDTO:
        return BookDTO(id=book.id, name=book.name)

    @staticmethod
    def from_dto(book_dto: BookDTO) -> Book:
        return Book(id=book_dto.id, name=book_dto.name, author=book_dto.author)
