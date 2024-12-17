from flask import Flask
from models.database import db
from routes.user_routes import user_routes
from routes.videogame_routes import videogame_routes
from routes.review_routes import review_routes  # Import review_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize database
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Creates database tables if they don't exist

    # Register blueprints
    app.register_blueprint(user_routes, url_prefix="/api")
    app.register_blueprint(videogame_routes, url_prefix="/api")
    app.register_blueprint(review_routes, url_prefix="/api") 

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=3000)
