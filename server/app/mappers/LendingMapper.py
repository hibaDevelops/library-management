from app.DTO.ClientDTO import ClientDTO
from app.DTO.LendingBookDTO import LendingBookDTO
from app.DTO.LendingDTO import LendingDTO
from app.Models.Lending import Lending


class LendingMapper:
    @staticmethod
    def to_dto(lending: Lending, client_dto: ClientDTO, book_dto: LendingBookDTO) -> LendingDTO:
        return LendingDTO(
            id=lending.id,
            client=client_dto,
            book=book_dto,
            lent_date=lending.lent_date,
            due_date=lending.due_date,
            return_date=lending.return_date,
            status=lending.status,
            created_at=lending.created_at,
            updated_at=lending.updated_at
        )
