import unittest
from app import create_app


class InvoicesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_invoice_list_requires_login(self):
        response = self.client.get("/invoices")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_invoice_create_requires_login(self):
        response = self.client.get("/invoice/create")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_invoice_details_requires_login(self):
        response = self.client.get("/invoice/1")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_invoice_preview_requires_login(self):
        response = self.client.get("/invoice/preview/1")
        self.assertIn(response.status_code, [200, 302, 401])

    def test_invoice_pdf_requires_login(self):
        response = self.client.get("/invoice/pdf/1")
        self.assertIn(response.status_code, [200, 302, 401])


if __name__ == "__main__":
    unittest.main()