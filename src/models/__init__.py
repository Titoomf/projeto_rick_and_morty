from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

import src.models.episode_model
import src.models.location_model
import src.models.character_model
import src.models.character_episode_model
