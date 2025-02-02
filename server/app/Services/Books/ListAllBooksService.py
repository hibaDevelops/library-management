from app.Models.Book import Book
from flask_injector import inject
from app.Repositories.BookRepository import BookRepository
from app.mappers.BookMapper import BookMapper


class ListAllBooksService:
    @inject
    def __init__(
        self, 
        book_repository: BookRepository
    ):
        self.book_repository = book_repository
    
    def list(self):
        books = self.book_repository.list_books()
        return [BookMapper.to_dto(book).to_dict() for book in books]
