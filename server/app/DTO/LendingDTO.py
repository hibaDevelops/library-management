from app.DTO.ClientDTO import ClientDTO
from app.DTO.LendingBookDTO import LendingBookDTO


class LendingDTO:
    def __init__(
        self,
        id: int,
        client: ClientDTO,
        book: LendingBookDTO,
        lent_date: str,
        due_date: str,
        return_date: str,
        status: str,
        created_at: str,
        updated_at: str,
    ):
        self.id = id
        self.client = client
        self.book = book
        self.lent_date = lent_date
        self.due_date = due_date
        self.return_date = return_date
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            'id': self.id,
            'client': self.client,
            'book': self.book,
            'lent_date': self.lent_date,
            'due_date': self.due_date,
            'return_date': self.return_date,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    def __repr__(self):
        return f"LendingDTO(id={self.id}'')"
