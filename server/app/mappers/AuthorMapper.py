from app.DTO.AuthorDTO import AuthorDTO
from app.Models.Author import Author


class AuthorMapper:
    @staticmethod
    def to_dto(author: Author) -> AuthorDTO | None:
        if author is None:
            return None
        else:
            return AuthorDTO(
                id=author.id,
                name=author.name
            )

    @staticmethod
    def from_dto(author_dto: AuthorDTO) -> Author:
        return Author(id=author_dto.id, name=author_dto.name)
