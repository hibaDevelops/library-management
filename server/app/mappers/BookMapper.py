from app.DTO.AuthorDTO import AuthorDTO
from app.DTO.BookDTO import BookDTO
from app.DTO.LendingBookDTO import LendingBookDTO
from app.DTO.PublisherDTO import PublisherDTO
from app.DTO.SaleBookDTO import SaleBookDTO
from app.Models.Book import Book
from app.Models.SaleBook import SaleBook


class BookMapper:
    @staticmethod
    def to_dto(book: Book, author: AuthorDTO or None, publisher: PublisherDTO or None) -> BookDTO:
        return BookDTO(
            id=book.id,
            name=book.name,
            available_copies_in_library=book.available_copies_in_library,
            available_copies_for_sale=book.available_copies_for_sale,
            price=book.price,
            library_location=book.library_location,
            bookstore_location=book.bookstore_location,
            language=book.language,
            photo=book.photo,
            created_at=book.created_at,
            updated_at=book.updated_at,
            author=author,
            publisher=publisher
        )

    @staticmethod
    def to_lending_book_dto(book: Book) -> LendingBookDTO:
        return LendingBookDTO(
            id=book.id,
            name=book.name,
        )

    @staticmethod
    def to_sale_book_dto(sale_book: SaleBook) -> SaleBookDTO:
        return SaleBookDTO(
            id=sale_book.book.id,
            name=sale_book.book.name,
            price=sale_book.book.price,
            quantity=sale_book.quantity
        )
