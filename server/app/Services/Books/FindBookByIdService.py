from flask_injector import inject

from app.Models.Book import Book
from app.Repositories.BookRepository import BookRepository


class FindBookByIdService:
    @inject
    def __init__(
        self,
        book_repository: BookRepository
    ):
        self.book_repository = book_repository

    def get(self, book_id: int) -> Book | None:
        return self.book_repository.get_by_id(book_id)
