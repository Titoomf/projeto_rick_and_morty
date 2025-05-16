from src.models import db


class CharacterEpisodeModel(db.Model):
    __tablename__ = "characters_episodes"

    character_id = db.Column(
        db.Integer, db.ForeignKey("characters.id"), primary_key=True
    )
    episode_id = db.Column(db.Integer, db.ForeignKey("episodes.id"), primary_key=True)

    def __repr__(self):
        return f"<CharacterEpisode {self.character_id}-{self.episode_id}>"
