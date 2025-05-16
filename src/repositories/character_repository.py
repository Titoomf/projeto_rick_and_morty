from src.models import db
import math
from src.models.character_model import Character


class CharacterRepository:

    def get_all_characters(self, name, page=1, per_page=20):
        try:
            query = Character.query

            if name:
                query = query.filter(Character.name.ilike(f"%{name}%"))

            total = query.count()  # total de resultados antes de aplicar limit/offset
            offset = (page - 1) * per_page
            characters = query.limit(per_page).offset(offset).all()

            # cálculo para número inteiro total de páginas

            total_pages = math.ceil(total / per_page)

            return {
                "items": characters,
                "total": total,
                "pages": total_pages,
                "page": page,
                "per_page": per_page,
            }

        except Exception:
            db.session.rollback()
            raise

    def get_character(self, id):
        try:
            character = db.session.get(Character, id)
            return character
        except Exception:
            db.session.rollback()
            raise
