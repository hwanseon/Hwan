from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # views/main_view.py에서 블루프린트 등록
    from .views.main_view import mainBP
    app.register_blueprint(mainBP)

    return app
