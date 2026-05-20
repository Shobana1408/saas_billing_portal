from models.payment import Payment
from models.invoice import Invoice


class BillingService:

    @staticmethod
    def create_payment(invoice_id, payment_method, payment_status, transaction_id, amount_paid):
        Payment.create(
            invoice_id=invoice_id,
            payment_method=payment_method,
            payment_status=payment_status,
            transaction_id=transaction_id,
            amount_paid=amount_paid
        )

        if payment_status == "success":
            Invoice.update_status(invoice_id, "paid")

        return {
            "status": True,
            "message": "Payment recorded successfully"
        }

    @staticmethod
    def get_payment_history():
        return Payment.get_all()

    @staticmethod
    def get_invoice_payments(invoice_id):
        return Payment.get_by_invoice(invoice_id)

    @staticmethod
    def calculate_tax(amount, tax_percentage=18):
        tax = (float(amount) * tax_percentage) / 100
        return round(tax, 2)

    @staticmethod
    def calculate_total_amount(amount, tax_percentage=18):
        tax = BillingService.calculate_tax(amount, tax_percentage)
        total = float(amount) + tax
        return round(total, 2)