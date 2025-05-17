from src.models import db, ma
from flask_marshmallow import Marshmallow


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

    @property
    def residents(self):
        return (self.characters_origin or []) + (self.characters_location or [])

    def __repr__(self):
        return f"<Location {self.name}>"


class LocationOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    dimension = ma.String()
    type = ma.String()
    residents = db.relationship(
        "Character", secondary="characters_location", back_populates="locations"
    )

    resident_count = ma.Method("get_resident_count")

    def get_resident_count(self, obj):
        return len(obj.residents) if obj.residents else 0
