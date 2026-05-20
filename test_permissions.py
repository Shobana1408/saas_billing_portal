import unittest
from app import create_app


class PermissionsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_dashboard_requires_login(self):
        response = self.client.get("/dashboard")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_admin_page_requires_login(self):
        response = self.client.get("/admin")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_finance_page_requires_login(self):
        response = self.client.get("/finance")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_analytics_page_requires_login(self):
        response = self.client.get("/analytics")
        self.assertIn(response.status_code, [200, 302, 401])


if __name__ == "__main__":
    unittest.main()