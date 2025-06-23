from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # ⚠️ Explicitly import models before db.create_all
    from .models import Hero, Power, HeroPower

    from .routes import api
    app.register_blueprint(api)

    with app.app_context():
        db.create_all()

    return app

