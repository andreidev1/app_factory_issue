import unittest
from app import create_app


class TestRoutes(unittest.TestCase):
    def test_index(self):
        flask_app = create_app()
        
        with flask_app.test_client() as test_client:
            
            response = test_client.get('/')
            print(response.data)
            assert response.status_code == 200