from app.DTO.BookDTO import BookDTO
from app.Models.Book import Book
from app.mappers.AuthorMapper import AuthorMapper
from app.mappers.BookMapper import BookMapper
from app.mappers.PublisherMapper import PublisherMapper


class BookTransformer:
    @staticmethod
    def transform(book: Book) -> BookDTO:
        author = AuthorMapper.to_dto(book.author).to_dict() if book.author is not None else None
        publisher = PublisherMapper.to_dto(book.publisher).to_dict() if book.publisher is not None else None
        return BookMapper.to_dto(book, author, publisher).to_dict()
