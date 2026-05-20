from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from app import mysql
from models.payment import Payment
from models.invoice import Invoice
from models.notification import Notification
from utils.decorators import role_required

billing_bp = Blueprint("billing", __name__)


@billing_bp.route("/billing")
@login_required
@role_required(1, 2, 3)
def billing_overview():
    invoice_summary = {
        "total": Invoice.total_invoices(),
        "paid": Invoice.paid_invoices(),
        "unpaid": Invoice.unpaid_invoices(),
        "overdue": Invoice.overdue_invoices(),
        "value": Invoice.total_invoice_value()
    }

    payment_summary = {
        "total": Payment.total_payments(),
        "success": Payment.successful_payments(),
        "failed": Payment.failed_payments(),
        "pending": Payment.pending_payments(),
        "amount": Payment.total_success_amount()
    }

    return render_template(
        "billing/billing_overview.html",
        invoice_summary=invoice_summary,
        payment_summary=payment_summary
    )


@billing_bp.route("/payments")
@login_required
@role_required(1, 2, 3)
def payment_history():
    payments = Payment.get_all()

    summary = {
        "total": Payment.total_payments(),
        "success": Payment.successful_payments(),
        "failed": Payment.failed_payments(),
        "pending": Payment.pending_payments(),
        "amount": Payment.total_success_amount()
    }

    return render_template(
        "billing/payment_history.html",
        payments=payments,
        summary=summary
    )


@billing_bp.route("/payment/create", methods=["GET", "POST"])
@login_required
@role_required(1, 3)
def payment_create():
    if request.method == "POST":
        invoice_id = request.form.get("invoice_id")
        payment_method = request.form.get("payment_method")
        payment_status = request.form.get("payment_status")
        transaction_id = request.form.get("transaction_id")
        amount_paid = request.form.get("amount_paid")

        Payment.create(
            invoice_id=invoice_id,
            payment_method=payment_method,
            payment_status=payment_status,
            transaction_id=transaction_id,
            amount_paid=amount_paid
        )

        invoice = Invoice.get_by_id(invoice_id)

        if payment_status == "success":
            Invoice.update_status(invoice_id, "paid")
        elif payment_status == "failed":
            Invoice.update_status(invoice_id, "unpaid")

        if invoice:
            company_id = invoice[1]
            invoice_number = invoice[4]

            cursor = mysql.connection.cursor()
            cursor.execute(
                """
                SELECT id
                FROM users
                WHERE company_id = %s
                """,
                (company_id,)
            )
            users = cursor.fetchall()
            cursor.close()

            for user in users:
                if payment_status == "success":
                    title = "Payment Successful"
                    message = f"Payment of ₹{amount_paid} for invoice {invoice_number} was successful."
                elif payment_status == "failed":
                    title = "Payment Failed"
                    message = f"Payment for invoice {invoice_number} failed. Please check billing details."
                else:
                    title = "Payment Pending"
                    message = f"Payment of ₹{amount_paid} for invoice {invoice_number} is pending."

                Notification.create(
                    user_id=user[0],
                    title=title,
                    message=message
                )

        flash("Payment saved successfully and notifications were sent.", "success")
        return redirect(url_for("billing.payment_history"))

    cursor = mysql.connection.cursor()
    cursor.execute(
        """
        SELECT 
            invoices.id,
            invoices.invoice_number,
            companies.company_name,
            invoices.total_amount,
            invoices.status
        FROM invoices
        JOIN companies ON invoices.company_id = companies.id
        ORDER BY invoices.created_at DESC
        """
    )
    invoices = cursor.fetchall()
    cursor.close()

    return render_template("billing/payment_create.html", invoices=invoices)


@billing_bp.route("/payment-failed")
@login_required
@role_required(1, 2, 3)
def payment_failed():
    return render_template("billing/payment_failed.html")


@billing_bp.route("/billing-settings", methods=["GET", "POST"])
@login_required
@role_required(1)
def billing_settings():
    if request.method == "POST":
        flash("Billing settings updated successfully.", "success")
        return redirect(url_for("billing.billing_settings"))

    return render_template("billing/billing_settings.html")