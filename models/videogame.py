from models.database import db

class VideoGame(db.Model):
    __tablename__ = "video_game"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    releaseDate = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "genre": self.genre, "releaseDate": self.releaseDate}
