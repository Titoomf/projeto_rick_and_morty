from werkzeug.exceptions import NotFound
from src.repositories.character_repository import CharacterRepository
from src.models.character_model import (
    character_output_all,
    character_output_by_id,
    Character,
)


class CharacterService:

    def __init__(self):
        self.character_repository = CharacterRepository()

    def get_all_characters(self, name, page=1):
        result = self.character_repository.get_all_characters(
            name,
            page,
        )
        data = character_output_all.dump(result["items"], many=True)

        return {
            "data": data,
            "page": result["page"],
            "per_page": result["per_page"],
            "total": result["total"],
            "pages": result["pages"],
        }

    def get_character(self, id):
        character = self.character_repository.get_character(id)
        if character is None:
            raise NotFound(f"Personagem com id {id} não encontrado")

        data = character_output_by_id.dump(character)
        return {
            "data": data,
        }
