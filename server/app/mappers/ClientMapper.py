from app.DTO.ClientDTO import ClientDTO
from app.Models.Client import Client


class ClientMapper:
    @staticmethod
    def to_dto(client: Client) -> ClientDTO:
        return ClientDTO(
            id=client.id,
            firstname=client.firstname,
            lastname=client.lastname,
            phone=client.phone,
            email=client.email,
            created_at=client.created_at,
            updated_at=client.updated_at,
        )
