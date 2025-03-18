from flask_injector import inject

from app.Repositories.BookRepository import BookRepository


class ListAllBooksService:
    @inject
    def __init__(
        self,
        book_repository: BookRepository
    ):
        self.book_repository = book_repository

    def list(self):
        return self.book_repository.list_books()
