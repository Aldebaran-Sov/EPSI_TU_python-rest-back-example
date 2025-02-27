import unittest
import requests
import service.api_igbd as api

class ApiigbdTestCase(unittest.TestCase):

    def test_get_token(self):
        response = api.get_token()
        self.assertEqual(response.status_code, 200)
