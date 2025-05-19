from src.models import db, ma
from flask_marshmallow import Marshmallow


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


class CharacterOutputAll(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    status = ma.String()
    species = ma.String()
    image = ma.String()


class CharacterOutputById(CharacterOutputAll):
    gender = ma.String()
    origin = ma.Nested("LocationOutput", allow_none=True)
    location = ma.Nested("LocationOutput", allow_none=True)

    latest_air_date = ma.Method("get_latest_air_date")

    def get_latest_air_date(self, obj):
        return obj.episodes[-1].air_date if obj.episodes else None


character_output_all = CharacterOutputAll(many=True)
character_output_by_id = CharacterOutputById()
