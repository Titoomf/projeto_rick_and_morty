from src.models import db, ma
from flask_marshmallow import Marshmallow

# from src.models.character_model import CharacterOutputAll


class Location(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    type = db.Column(db.String(100))
    dimension = db.Column(db.String(100))

    characters_origin = db.relationship(
        "Character", foreign_keys="Character.origin_id", back_populates="origin"
    )

    characters_location = db.relationship(
        "Character", foreign_keys="Character.location_id", back_populates="location"
    )

    def __repr__(self):
        return f"<Location {self.name}>"


class LocationOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    dimension = ma.String()
    type = ma.String()
    resident = ma.Method("get_resident_count")

    def get_resident_count(self, obj):
        return len(obj.characters_location) if obj.characters_location else 0
