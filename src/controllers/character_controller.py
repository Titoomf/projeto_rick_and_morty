import traceback
from werkzeug.exceptions import NotFound
from flask import jsonify
from src.services.character_service import CharacterService
from marshmallow.exceptions import ValidationError
from src.utils.response_api import ApiResponse


class CharacterController:

    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self, name, page=1):
        try:
            data = self.character_service.get_all_characters(name, page=page)
            return ApiResponse.response(
                True, "Personagens recuperados com sucesso.", data, 200
            )
        except Exception:
            traceback.print_exc()
            return ApiResponse.response(
                False, "Erro ao recuperar personagens.", None, 500
            )

    def get_character(self, id):
        try:
            data = self.character_service.get_character(id)

            return ApiResponse.response(
                True, "Personagem recuperado com sucesso.", data, 200
            )

        except NotFound as nf:
            return ApiResponse.response(False, str(nf), None, 404)

        except Exception:
            traceback.print_exc()
            return ApiResponse.response(
                False, "Erro ao recuperar personagem.", None, 500
            )
