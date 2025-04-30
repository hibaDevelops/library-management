from app.DTO.ClientDTO import ClientDTO
from app.Models.Client import Client
from app.mappers.ClientMapper import ClientMapper


class ClientTransformer:
    @staticmethod
    def transform(client: Client) -> ClientDTO:
        return ClientMapper.to_dto(client).to_dict()
