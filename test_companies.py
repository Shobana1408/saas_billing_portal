import unittest
from app import create_app


class CompaniesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_company_list_requires_login(self):
        response = self.client.get("/companies")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_company_create_requires_login(self):
        response = self.client.get("/company/create")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_company_details_requires_login(self):
        response = self.client.get("/company/1")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_company_edit_requires_login(self):
        response = self.client.get("/company/edit/1")
        self.assertIn(response.status_code, [200, 302, 401])


if __name__ == "__main__":
    unittest.main()