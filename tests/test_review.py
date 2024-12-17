import unittest
from app import create_app
from models.database import db
from models.review import Review

class ReviewTestCase(unittest.TestCase):
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

    def test_create_review(self):
        response = self.client.post("/api/reviews", json={"title": "Great Game", "rating": 9, "comment": "Loved it!"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Great Game", str(response.data))

    def test_get_reviews(self):
        self.client.post("/api/reviews", json={"title": "Great Game", "rating": 9, "comment": "Loved it!"})
        response = self.client.get("/api/reviews")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Great Game", str(response.data))

    def test_filter_reviews_by_rating(self):
        self.client.post("/api/reviews", json={"title": "Great Game", "rating": 9, "comment": "Loved it!"})
        self.client.post("/api/reviews", json={"title": "Bad Game", "rating": 3, "comment": "Hated it!"})
        response = self.client.get("/api/reviews?rating=8-10")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Great Game", str(response.data))
        self.assertNotIn("Bad Game", str(response.data))

    def test_mark_review_as_helpful(self):
        self.client.post("/api/reviews", json={"title": "Great Game", "rating": 9, "comment": "Loved it!"})
        response = self.client.post("/api/reviews/1/helpful")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Marked as helpful", str(response.data))

    def test_update_review(self):
        self.client.post("/api/reviews", json={"title": "Great Game", "rating": 9, "comment": "Loved it!"})
        response = self.client.put("/api/reviews/1", json={"title": "Amazing Game"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Amazing Game", str(response.data))

    def test_delete_review(self):
        self.client.post("/api/reviews", json={"title": "Great Game", "rating": 9, "comment": "Loved it!"})
        response = self.client.delete("/api/reviews/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Review deleted successfully", str(response.data))

    def test_get_average_rating(self):
        self.client.post("/api/reviews", json={"title": "Great Game", "rating": 9, "comment": "Loved it!"})
        self.client.post("/api/reviews", json={"title": "Good Game", "rating": 7, "comment": "Liked it!"})
        response = self.client.get("/api/reviews/average")
        self.assertEqual(response.status_code, 200)
        self.assertIn("8.0", str(response.data))

    def test_add_comment_to_review(self):
        self.client.post("/api/reviews", json={"title": "Great Game", "rating": 9, "comment": "Loved it!"})
        response = self.client.post("/api/reviews/1/comments", json={"comment": "I agree!"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("I agree!", str(response.data))

if __name__ == "__main__":
    unittest.main()
