from src.models import db
from sqlalchemy.exc import SQLAlchemyError
import math
from src.models.character_model import Character


class CharacterRepository:

    def get_all_characters(self, name=None, page=1, per_page=20):
        try:
            query = Character.query

            if name:
                query = query.filter(Character.name.ilike(f"%{name}%"))

            total = query.count()
            offset = (page - 1) * per_page
            characters = query.limit(per_page).offset(offset).all()
            total_pages = math.ceil(total / per_page)

            return {
                "items": characters,
                "total": total,
                "pages": total_pages,
                "page": page,
                "per_page": per_page,
            }

        except SQLAlchemyError:
            db.session.rollback()
            raise

    def get_character(self, id):
        try:
            return db.session.get(Character, id)
        except SQLAlchemyError:
            db.session.rollback()
            raise
