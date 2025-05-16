from src.models import db, ma


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
    air_date = ma.String()
    episode = ma.String()
