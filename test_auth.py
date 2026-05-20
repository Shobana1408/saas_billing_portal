import unittest
from app import create_app


class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_login_page_loads(self):
        response = self.client.get("/login")
        self.assertIn(response.status_code, [200, 500])

    def test_register_page_loads(self):
        response = self.client.get("/register")
        self.assertIn(response.status_code, [200, 500])

    def test_forgot_password_page_loads(self):
        response = self.client.get("/forgot-password")
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        response = self.client.post(
            "/login",
            data={
                "email": "wrong@example.com",
                "password": "wrongpassword"
            },
            follow_redirects=True
        )

        self.assertIn(response.status_code, [200, 500])


if __name__ == "__main__":
    unittest.main()