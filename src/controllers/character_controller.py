import traceback
from flask import jsonify
from src.services.character_service import CharacterService
from marshmallow.exceptions import ValidationError
from src.utils.response_api import ApiResponse


class CharacterController:

    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self, name, page=1, per_page=20):
        try:
            data = self.character_service.get_all_characters(
                name, page=page, per_page=per_page
            )
            return ApiResponse.response(
                True, "Personagens recuperados com sucesso.", data
            )
        except Exception:
            traceback.print_exc()
            return ApiResponse.response(
                False, "Erro ao recuperar personagens.", None, 500
            )

    def get_character(self, id):
        try:
            data = self.character_service.get_character(id)
            if not data:
                return ApiResponse.response(
                    False, f"Nenhum personagem encontrado com ID={id}.", None, 404
                )

            return ApiResponse.response(
                True, "Personagem recuperado com sucesso.", data
            )
        except ValidationError as ve:
            return ApiResponse.response(False, f"Erro de validação: {ve}", None, 400)
        except Exception:
            traceback.print_exc()
            return ApiResponse.response(
                False, "Erro ao recuperar personagem.", None, 500
            )
