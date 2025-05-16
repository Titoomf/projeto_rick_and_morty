from flask import Flask
from config.settings import DATABASE_URI
from src.models import db, ma
from src.routes.character_routes import character_bp


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MOTIFICATIONS"] = False
# db.init(app)


db.init_app(app)
ma.init_app(app)

app.register_blueprint(character_bp, url_prefix="/character")


if __name__ == "__main__":
    app.run(debug=True)
