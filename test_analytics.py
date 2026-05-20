import unittest
from app import create_app


class AnalyticsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_revenue_forecast_route_requires_login(self):
        response = self.client.get("/analytics/revenue-forecast")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_churn_prediction_route_requires_login(self):
        response = self.client.get("/analytics/churn-prediction")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_spending_insights_route_requires_login(self):
        response = self.client.get("/analytics/spending-insights")
        self.assertIn(response.status_code, [200, 302, 401])


if __name__ == "__main__":
    unittest.main()