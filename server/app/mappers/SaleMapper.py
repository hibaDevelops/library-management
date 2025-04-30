from app.DTO.ClientDTO import ClientDTO
from app.DTO.SaleBookDTO import SaleBookDTO
from app.DTO.SaleDTO import SaleDTO
from app.Models.Sale import Sale


class SaleMapper:
    @staticmethod
    def calculate_total_amount(books_dto: list[SaleBookDTO], sale: Sale):
        total_amount = 0
        for book in books_dto:
            total_amount += book.quantity * book.price

        return total_amount

    @staticmethod
    def to_dto(sale: Sale, client_dto: ClientDTO, books_dto: list[SaleBookDTO]) -> SaleDTO:
        return SaleDTO(
            id=sale.id,
            client=client_dto,
            books=books_dto,
            sale_date=sale.sale_date,
            return_date=sale.return_date,
            status=sale.status,
            total_discount=sale.total_discount,
            total_amount=SaleMapper.calculate_total_amount(books_dto, sale),
            created_at=sale.created_at,
            updated_at=sale.updated_at
        )
