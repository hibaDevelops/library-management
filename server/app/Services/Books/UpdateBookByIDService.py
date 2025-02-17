from flask_injector import inject

from app.Exceptions.not_found_exception import NotFoundException
from app.Models.Book import Book
from app.Repositories.AuthorRepository import AuthorRepository
from app.Repositories.BookRepository import BookRepository
from app.Repositories.PublisherRepository import PublisherRepository


class UpdateBookByIDService:
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

    def update(
        self,
        book_id: int,
        name: str = None,
        available_copies_in_library: int = None,
        available_copies_for_sale: int = None,
        price: float = None,
        location: str = None,
        author_id: int = None,
        publisher_id: int = None
    ) -> Book:
        book = self.book_repository.get_by_id(book_id)
        if not book:
            raise NotFoundException(f"Book with ID {book_id} does not exist")
        if author_id:
            author = self.author_repository.get_by_id(author_id)
            if not author:
                raise NotFoundException(f"Author with ID {author_id} does not exist")

        if publisher_id:
            publisher = self.publisher_repository.get_by_id(publisher_id)
            if not publisher:
                raise NotFoundException(f"Publisher with ID {publisher_id} does not exist")

        update_fields = {}
        if name is not None:
            update_fields['name'] = name
        if available_copies_in_library is not None:
            update_fields['available_copies_in_library'] = available_copies_in_library
        if available_copies_for_sale is not None:
            update_fields['available_copies_for_sale'] = available_copies_for_sale
        if price is not None:
            update_fields['price'] = price
        if location is not None:
            update_fields['location'] = location
        if author_id is not None:
            update_fields['author_id'] = author_id
        if publisher_id is not None:
            update_fields['publisher_id'] = publisher_id

        return self.book_repository.update(book, update_fields)
