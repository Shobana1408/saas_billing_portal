import unittest
from app import create_app


class SubscriptionsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_plans_requires_login(self):
        response = self.client.get("/plans")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_subscription_list_requires_login(self):
        response = self.client.get("/subscriptions")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_subscription_create_requires_login(self):
        response = self.client.get("/subscription/create")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_subscription_details_requires_login(self):
        response = self.client.get("/subscription/1")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_upgrade_plan_requires_login(self):
        response = self.client.get("/subscription/upgrade/1")
        self.assertIn(response.status_code, [200, 302, 401])


if __name__ == "__main__":
    unittest.main()