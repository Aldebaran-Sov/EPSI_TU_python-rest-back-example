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
