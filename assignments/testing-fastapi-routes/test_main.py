import unittest

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


class TestBookApi(unittest.TestCase):
    def test_list_books_returns_json_list(self):
        response = client.get("/books")

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)


if __name__ == "__main__":
    unittest.main()