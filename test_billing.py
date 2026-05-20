import unittest
from app import create_app


class BillingTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_billing_overview_requires_login(self):
        response = self.client.get("/billing")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_payment_history_requires_login(self):
        response = self.client.get("/payments")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_payment_create_requires_login(self):
        response = self.client.get("/payment/create")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_payment_failed_page_requires_login(self):
        response = self.client.get("/payment-failed")
        self.assertIn(response.status_code, [200, 302, 401])


if __name__ == "__main__":
    unittest.main()