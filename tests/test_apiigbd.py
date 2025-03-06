import unittest
import services.api_igbd as api

class ApiigbdTestCase(unittest.TestCase):

    def test_get_auth_response(self):
        response = api.get_auth_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
    
    def test_get_auth_token(self):
        token = api.get_auth_token()
        self.assertEqual(type(token), str)
    
    def test_get_videogame(self):    
        name = "Baldur's Gate 3"
        genres = [12, 15,16, 24, 31]
        data = api.get_videogame(name)
        self.assertEqual(data["name"], name)
        self.assertIn("genres", data)
        self.assertIsInstance(data["genres"], list)
        self.assertEqual(data["genres"], genres)

