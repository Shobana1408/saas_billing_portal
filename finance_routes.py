from flask import Blueprint, render_template
from flask_login import login_required

from models.payment import Payment
from models.invoice import Invoice
from models.analytics import Analytics
from utils.decorators import role_required

finance_bp = Blueprint("finance", __name__)


@finance_bp.route("/finance")
@login_required
@role_required(1, 3)
def finance_home():
    finance_summary = {
        "total_revenue": Analytics.total_revenue(),
        "failed_payments": Analytics.failed_payments(),
        "total_payments": Payment.total_payments(),
        "successful_payments": Payment.successful_payments(),
        "pending_payments": Payment.pending_payments(),
        "total_invoices": Invoice.total_invoices(),
        "paid_invoices": Invoice.paid_invoices(),
        "unpaid_invoices": Invoice.unpaid_invoices(),
        "overdue_invoices": Invoice.overdue_invoices(),
        "total_invoice_value": Invoice.total_invoice_value(),
        "collected_amount": Payment.total_success_amount()
    }

    return render_template(
        "finance/finance_home.html",
        finance_summary=finance_summary
    )


@finance_bp.route("/finance/transactions")
@login_required
@role_required(1, 3)
def transaction_list():
    payments = Payment.get_all()

    summary = {
        "total": Payment.total_payments(),
        "success": Payment.successful_payments(),
        "failed": Payment.failed_payments(),
        "pending": Payment.pending_payments(),
        "amount": Payment.total_success_amount()
    }

    return render_template(
        "finance/transaction_list.html",
        payments=payments,
        summary=summary
    )


@finance_bp.route("/finance/expenses")
@login_required
@role_required(1, 3)
def expense_tracking():
    expenses = [
        {
            "expense_id": "EXP-001",
            "category": "Server Hosting",
            "amount": 15000,
            "month": "May",
            "status": "Paid"
        },
        {
            "expense_id": "EXP-002",
            "category": "Marketing",
            "amount": 20000,
            "month": "May",
            "status": "Paid"
        },
        {
            "expense_id": "EXP-003",
            "category": "Software Tools",
            "amount": 10000,
            "month": "May",
            "status": "Pending"
        },
        {
            "expense_id": "EXP-004",
            "category": "Cloud Storage",
            "amount": 12000,
            "month": "June",
            "status": "Paid"
        }
    ]

    total_expenses = sum(expense["amount"] for expense in expenses)
    paid_expenses = sum(expense["amount"] for expense in expenses if expense["status"] == "Paid")
    pending_expenses = sum(expense["amount"] for expense in expenses if expense["status"] == "Pending")

    summary = {
        "total_expenses": total_expenses,
        "paid_expenses": paid_expenses,
        "pending_expenses": pending_expenses,
        "expense_count": len(expenses)
    }

    return render_template(
        "finance/expense_tracking.html",
        expenses=expenses,
        summary=summary
    )


@finance_bp.route("/finance/revenue")
@login_required
@role_required(1, 3)
def revenue_tracking():
    monthly_revenue = Analytics.monthly_revenue()

    summary = {
        "total_revenue": Analytics.total_revenue(),
        "successful_payments": Payment.successful_payments(),
        "failed_payments": Payment.failed_payments(),
        "pending_payments": Payment.pending_payments()
    }

    return render_template(
        "finance/revenue_tracking.html",
        monthly_revenue=monthly_revenue,
        summary=summary
    )


@finance_bp.route("/finance/tax-reports")
@login_required
@role_required(1, 3)
def tax_reports():
    invoices = Invoice.get_all()

    total_tax = 0
    total_amount = 0
    paid_tax = 0
    unpaid_tax = 0

    for invoice in invoices:
        tax = float(invoice[4])
        amount = float(invoice[5])
        status = invoice[7]

        total_tax += tax
        total_amount += amount

        if status == "paid":
            paid_tax += tax
        else:
            unpaid_tax += tax

    summary = {
        "total_tax": round(total_tax, 2),
        "paid_tax": round(paid_tax, 2),
        "unpaid_tax": round(unpaid_tax, 2),
        "total_amount": round(total_amount, 2),
        "total_invoices": len(invoices)
    }

    return render_template(
        "finance/tax_reports.html",
        invoices=invoices,
        summary=summary
    )