from src.models import db, ma
from marshmallow import fields
from datetime import datetime


class Character(db.Model):
    __tablename__ = "characters"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(255), nullable=True)

    origin_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))

    origin = db.relationship(
        "Location", foreign_keys=[origin_id], back_populates="characters_origin"
    )

    location = db.relationship(
        "Location", foreign_keys=[location_id], back_populates="characters_location"
    )

    episodes = db.relationship(
        "Episode", secondary="characters_episodes", back_populates="characters"
    )

    def __repr__(self):
        return f"<Character {self.name}>"


class CharacterOutputById(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    image = ma.String()
    species = ma.String()
    status = ma.String()

    latest_air_date = ma.Function(lambda obj: get_latest_air_date(obj))


def get_latest_air_date(character):
    if not character.episodes:
        return None
    try:
        # Filtra episódios com data válida
        valid_episodes = [ep for ep in character.episodes if ep.air_date]
        if not valid_episodes:
            return None
        # Ordena pelo air_date convertida para datetime
        latest_episode = max(
            valid_episodes, key=lambda ep: datetime.strptime(ep.air_date, "%B %d, %Y")
        )
        return latest_episode.air_date
    except Exception:
        return None


class CharacterOutputAll(CharacterOutputById):
    gender = ma.String()
    origin = ma.Nested("LocationOutput", allow_none=True)
    location = ma.Nested("LocationOutput", allow_none=True)


character_output_all = CharacterOutputAll(many=True)
character_output_by_id = CharacterOutputById()

#     latest_air_date = ma.Function(lambda obj: obj.episodes[-1].air_date if obj.episodes else None)
