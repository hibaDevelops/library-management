from app.DTO.PublisherDTO import PublisherDTO
from app.Models.Publisher import Publisher

class PublisherMapper:
    @staticmethod
    def to_dto(publisher: Publisher) -> PublisherDTO | None:
        if publisher is None:
            return None
        else:
            return PublisherDTO(
                id=publisher.id,
                name=publisher.name
            )

    @staticmethod
    def from_dto(publisher_dto: PublisherDTO) -> Publisher:
        return Publisher(id=publisher_dto.id, name=publisher_dto.name)
