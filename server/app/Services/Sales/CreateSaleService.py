from flask_injector import inject
from sqlalchemy.exc import SQLAlchemyError

from app.Exceptions.OutOfStockException import OutOfStockException
from app.Exceptions.not_found_exception import NotFoundException
from app.Models.Sale import Sale
from app.Repositories.BookRepository import BookRepository
from app.Repositories.ClientRepository import ClientRepository
from app.Repositories.SaleBookRepository import SaleBookRepository
from app.Repositories.SaleRepository import SaleRepository
from database import MySQLDB


class CreateSaleService:
    @inject
    def __init__(
        self,
        sale_repository: SaleRepository,
        client_repository: ClientRepository,
        book_repository: BookRepository,
        sale_book_repository: SaleBookRepository,
        db: MySQLDB
    ):
        self.sale_repository = sale_repository
        self.client_repository = client_repository
        self.book_repository = book_repository
        self.sale_book_repository = sale_book_repository
        self.db = db

    def create(
        self,
        client_id: int,
        book_id: int,
        sale_date: str,
        quantity: int,
        status: str,
        discount: float = 0.00,
    ) -> Sale:
        try:
            client = self.client_repository.get_by_id(client_id)
            if not client:
                raise NotFoundException(f"Client with ID {client_id} does not exist")

            book = self.book_repository.get_by_id(book_id)
            if not book:
                raise NotFoundException(f"Book with ID {book_id} does not exist")
            if book.available_copies_for_sale == 0:
                raise OutOfStockException(f"This Book '{book.name}' is currently out of stock")
            if book.available_copies_for_sale < quantity:
                raise OutOfStockException(f"This Book '{book.name}' does not have enough copies available for sale")

            sale = self.sale_repository.create(
                client_id,
                sale_date,
                status,
                discount
            )

            self.sale_book_repository.create(
                sale.id,
                book_id,
                quantity
            )

            update_fields = {'available_copies_for_sale': book.available_copies_for_sale - quantity}
            self.book_repository.update(book, update_fields)

            self.db.session.commit()

        except SQLAlchemyError as e:
            self.db.session.rollback()
            raise e
        except Exception as e:
            self.db.session.rollback()
            raise e

        new_sale = self.sale_repository.get_by_id(sale.id)
        return new_sale
