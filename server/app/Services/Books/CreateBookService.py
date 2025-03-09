from flask_injector import inject

from app.Exceptions.not_found_exception import NotFoundException
from app.Models.Book import Book
from app.Repositories.AuthorRepository import AuthorRepository
from app.Repositories.BookRepository import BookRepository
from app.Repositories.PublisherRepository import PublisherRepository


class CreateBookService:
    @inject
    def __init__(
        self,
        book_repository: BookRepository,
        author_repository: AuthorRepository,
        publisher_repository: PublisherRepository,
    ):
        self.book_repository = book_repository
        self.author_repository = author_repository
        self.publisher_repository = publisher_repository

    def create(
        self,
        name: str,
        available_copies_in_library: int,
        available_copies_for_sale: int,
        price: float = None,
        location: str = None,
        language: str = None,
        photo: str = None,
        author_id: int = None,
        publisher_id: int = None
    ) -> Book:
        if author_id:
            author = self.author_repository.get_by_id(author_id)
            if not author:
                raise NotFoundException(f"Author with ID {author_id} does not exist")

        if publisher_id:
            publisher = self.publisher_repository.get_by_id(publisher_id)
            if not publisher:
                raise NotFoundException(f"Publisher with ID {publisher_id} does not exist")

        return self.book_repository.create(
            name,
            available_copies_in_library,
            available_copies_for_sale,
            price,
            location,
            language,
            photo,
            author_id,
            publisher_id
        )
