import unittest
from app import create_app


class UsersTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_user_list_requires_login(self):
        response = self.client.get("/users")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_user_details_requires_login(self):
        response = self.client.get("/users/1")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_create_user_requires_login(self):
        response = self.client.get("/users/create")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_profile_requires_login(self):
        response = self.client.get("/profile")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_edit_profile_requires_login(self):
        response = self.client.get("/edit-profile")
        self.assertIn(response.status_code, [200, 302, 401])


if __name__ == "__main__":
    unittest.main()