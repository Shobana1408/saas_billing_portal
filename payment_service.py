from models.payment import Payment
from models.invoice import Invoice


class PaymentService:

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
            "message": "Payment created successfully"
        }

    @staticmethod
    def get_all_payments():
        return Payment.get_all()

    @staticmethod
    def get_payment_details(payment_id):
        return Payment.get_by_id(payment_id)

    @staticmethod
    def get_payments_by_invoice(invoice_id):
        return Payment.get_by_invoice(invoice_id)

    @staticmethod
    def get_payment_status_message(payment_status):
        if payment_status == "success":
            return "Payment completed successfully"
        elif payment_status == "failed":
            return "Payment failed. Please try again"
        else:
            return "Payment is pending"