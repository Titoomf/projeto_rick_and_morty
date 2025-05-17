from src.models import db, ma
from marshmallow import validate


class Episode(db.Model):
    __tablename__ = "episodes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    air_date = db.Column(db.String(50), nullable=False)
    episode = db.Column(db.String(50), nullable=False)

    characters = db.relationship(
        "Character", secondary="characters_episodes", back_populates="episodes"
    )

    def __repr__(self):
        return f"<Episode {self.name}>"
