from app.DTO.LendingDTO import LendingDTO
from app.Models.Lending import Lending
from app.mappers.BookMapper import BookMapper
from app.mappers.ClientMapper import ClientMapper
from app.mappers.LendingMapper import LendingMapper


class LendingTransformer:
    @staticmethod
    def transform(lending: Lending) -> LendingDTO:
        client = ClientMapper.to_dto(lending.client).to_dict()
        books_dto = [BookMapper.to_lending_book_dto(book).to_dict() for book in lending.books]
        return LendingMapper.to_dto(lending, client, books_dto).to_dict()
