from flask import Blueprint, request, jsonify
from models.database import db
from models.videogame import VideoGame

videogame_routes = Blueprint("videogame_routes", __name__)

@videogame_routes.route("/videogames", methods=["GET"])
def get_videogames():
    videoGames = VideoGame.query.all()
    return jsonify([videoGame.to_dict() for videoGame in videoGames]), 200

@videogame_routes.route("/videogames/<int:videoGame_id>", methods=["GET"])
def get_videogame(videoGame_id):
    videoGame = VideoGame.query.get(videoGame_id)
    if videoGame:
        return jsonify(videoGame.to_dict()), 200
    return jsonify({"error": "VideoGame not found"}), 404

@videogame_routes.route("/videogames", methods=["POST"])
def create_videogame():
    data = request.get_json()
    if not data.get("title") or not data.get("genre") or not data.get("releaseDate"):
        return jsonify({"error": "Title, genre, and releaseDate are required"}), 400

    new_videoGame = VideoGame(title=data["title"], genre=data["genre"], releaseDate=data["releaseDate"])
    db.session.add(new_videoGame)
    db.session.commit()
    return jsonify(new_videoGame.to_dict()), 201

@videogame_routes.route("/videogames/<int:videoGame_id>", methods=["PUT"])
def update_videogame(videoGame_id):
    videoGame = VideoGame.query.get(videoGame_id)
    if not videoGame:
        return jsonify({"error": "VideoGame not found"}), 404

    data = request.get_json()
    videoGame.title = data.get("title", videoGame.title)
    videoGame.genre = data.get("genre", videoGame.genre)
    videoGame.releaseDate = data.get("releaseDate", videoGame.releaseDate)
    db.session.commit()
    return jsonify(videoGame.to_dict()), 200

@videogame_routes.route("/videogames/<int:videoGame_id>", methods=["DELETE"])
def delete_videogame(videoGame_id):
    videoGame = VideoGame.query.get(videoGame_id)
    if not videoGame:
        return jsonify({"error": "VideoGame not found"}), 404

    db.session.delete(videoGame)
    db.session.commit()
    return jsonify({"message": "VideoGame deleted successfully"}), 200
