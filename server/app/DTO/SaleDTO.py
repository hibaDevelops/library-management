from app.DTO.ClientDTO import ClientDTO
from app.DTO.SaleBookDTO import SaleBookDTO


class SaleDTO:
    def __init__(
        self,
        id: int,
        client: ClientDTO,
        books: list[SaleBookDTO],
        sale_date: str,
        return_date: str,
        status: str,
        created_at: str,
        updated_at: str,
        total_discount: float = 0.00,
        total_amount: float = 0.00,
    ):
        self.id = id
        self.client = client
        self.books = books
        self.sale_date = sale_date
        self.return_date = return_date
        self.total_discount = total_discount
        self.total_amount = total_amount
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        client_dict = self.client.to_dict() if isinstance(self.client, ClientDTO) else self.client
        books_dict = [book.to_dict() for book in self.books] if isinstance(self.books, list) else self.books

        return {
            'id': self.id,
            'client': client_dict,
            'books': books_dict,
            'sale_date': self.sale_date,
            'return_date': self.return_date,
            'total_discount': self.total_discount,
            'total_amount': self.total_amount,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    def __repr__(self):
        return f"SaleDTO(id={self.id}'')"
