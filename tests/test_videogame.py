import unittest
from app import create_app
from models.database import db
from models.videogame import VideoGame

class VideogameTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_videogame(self):
        response = self.client.post("/api/videogames", json={"title": "Super Mario Bros.", "genre": "Platformer", "releaseDate": "1985-09-13"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Super Mario Bros.", str(response.data))

    def test_get_videogames(self):
        self.client.post("/api/videogames", json={"title": "Super Mario Bros.", "genre": "Platformer", "releaseDate": "1985-09-13"})
        response = self.client.get("/api/videogames")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Super Mario Bros.", str(response.data))

    def test_get_videogame(self):
        self.client.post("/api/videogames", json={"title": "Super Mario Bros.", "genre": "Platformer", "releaseDate": "1985-09-13"})
        response = self.client.get("/api/videogames/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Super Mario Bros.", str(response.data))

    def test_update_videogame(self):
        self.client.post("/api/videogames", json={"title": "Super Mario Bros.", "genre": "Platformer", "releaseDate": "1985-09-13"})
        response = self.client.put("/api/videogames/1", json={"title": "The Legend of Zelda"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("The Legend of Zelda", str(response.data))

    def test_delete_videogame(self):
        self.client.post("/api/videogames", json={"title": "Super Mario Bros.", "genre": "Platformer", "releaseDate": "1985-09-13"})
        response = self.client.delete("/api/videogames/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("VideoGame deleted successfully", str(response.data))

if __name__ == '__main__':
    unittest.main()
