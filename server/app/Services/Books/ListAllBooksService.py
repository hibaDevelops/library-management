from app.Models.Book import Book
from flask_injector import inject
from app.Repositories.BookRepository import BookRepository
from app.mappers.BookMapper import BookMapper
from app.mappers.AuthorMapper import AuthorMapper
from app.mappers.PublisherMapper import PublisherMapper


class ListAllBooksService:
    @inject
    def __init__(
        self, 
        book_repository: BookRepository
    ):
        self.book_repository = book_repository
    
    def list(self):
        books = self.book_repository.list_books()
        for book in books:
            author = AuthorMapper.to_dto(book.author).to_dict()
            publisher = PublisherMapper.to_dto(book.publisher).to_dict()
            return BookMapper.to_dto(book, author, publisher).to_dict()
