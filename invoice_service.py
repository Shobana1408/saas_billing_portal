from datetime import datetime
from models.invoice import Invoice
from services.billing_service import BillingService


class InvoiceService:

    @staticmethod
    def generate_invoice_number():
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"INV-{current_time}"

    @staticmethod
    def create_invoice(company_id, subscription_id, amount, due_date, status="unpaid"):
        tax = BillingService.calculate_tax(amount)
        total_amount = BillingService.calculate_total_amount(amount)
        invoice_number = InvoiceService.generate_invoice_number()

        Invoice.create(
            company_id=company_id,
            subscription_id=subscription_id,
            invoice_number=invoice_number,
            amount=amount,
            tax=tax,
            total_amount=total_amount,
            due_date=due_date,
            status=status
        )

        return {
            "status": True,
            "message": "Invoice created successfully",
            "invoice_number": invoice_number,
            "tax": tax,
            "total_amount": total_amount
        }

    @staticmethod
    def get_all_invoices():
        return Invoice.get_all()

    @staticmethod
    def get_invoice_details(invoice_id):
        return Invoice.get_by_id(invoice_id)

    @staticmethod
    def update_invoice_status(invoice_id, status):
        Invoice.update_status(invoice_id, status)

        return {
            "status": True,
            "message": "Invoice status updated successfully"
        }

    @staticmethod
    def delete_invoice(invoice_id):
        Invoice.delete(invoice_id)

        return {
            "status": True,
            "message": "Invoice deleted successfully"
        }