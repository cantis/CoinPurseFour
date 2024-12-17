import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

load_dotenv('.env')


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__, template_folder=os.path.join('src', 'templates'))

    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'default_secret_key_sesame')

    # Initialize database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route('/')
    def home() -> str:
        """Render the home page."""
        return render_template('home.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
