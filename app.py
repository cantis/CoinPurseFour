import os

from flask import Flask, render_template


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__, template_folder=os.path.join('src', 'templates'))

    @app.route('/')
    def home() -> str:
        """Render the home page."""
        return render_template('home.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
