from app.DTO.SaleDTO import SaleDTO
from app.Models.Sale import Sale
from app.mappers.BookMapper import BookMapper
from app.mappers.ClientMapper import ClientMapper
from app.mappers.SaleMapper import SaleMapper


class SaleTransformer:
    @staticmethod
    def transform(sale: Sale) -> SaleDTO:
        client = ClientMapper.to_dto(sale.client).to_dict()
        books_dto = [BookMapper.to_sale_book_dto(sale_book) for sale_book in sale.sale_books]
        return SaleMapper.to_dto(sale, client, books_dto).to_dict()
