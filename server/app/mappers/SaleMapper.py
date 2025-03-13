from app.DTO.ClientDTO import ClientDTO
from app.DTO.SaleBookDTO import SaleBookDTO
from app.DTO.SaleDTO import SaleDTO
from app.Models.Sale import Sale


class SaleMapper:
    @staticmethod
    def calculate_total_amount(books_dto: list[SaleBookDTO], sale: Sale):
        total_before_discount = 0
        for book in books_dto:
            print(book.name)
            total_before_discount += book.quantity * book.price

        # Apply the discount to the total amount
        total_after_discount = total_before_discount - sale.total_discount
        return total_after_discount

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
