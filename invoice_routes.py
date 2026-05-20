from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from app import mysql
from models.invoice import Invoice
from models.notification import Notification
from utils.decorators import role_required

invoice_bp = Blueprint("invoices", __name__)


@invoice_bp.route("/invoices")
@login_required
@role_required(1, 2, 3)
def invoice_list():
    invoices = Invoice.get_all()

    summary = {
        "total": Invoice.total_invoices(),
        "paid": Invoice.paid_invoices(),
        "unpaid": Invoice.unpaid_invoices(),
        "overdue": Invoice.overdue_invoices(),
        "value": Invoice.total_invoice_value()
    }

    return render_template(
        "invoices/invoice_list.html",
        invoices=invoices,
        summary=summary
    )


@invoice_bp.route("/invoice/create", methods=["GET", "POST"])
@login_required
@role_required(1, 3)
def invoice_create():
    if request.method == "POST":
        company_id = request.form.get("company_id")
        subscription_id = request.form.get("subscription_id")
        invoice_number = request.form.get("invoice_number")
        amount = float(request.form.get("amount"))
        tax = float(request.form.get("tax"))
        total_amount = float(request.form.get("total_amount"))
        due_date = request.form.get("due_date")
        status = request.form.get("status")

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
            Notification.create(
                user_id=user[0],
                title="New Invoice Generated",
                message=f"Invoice {invoice_number} has been generated with total amount ₹{total_amount}."
            )

        flash("Invoice created successfully and notifications were sent.", "success")
        return redirect(url_for("invoices.invoice_list"))

    cursor = mysql.connection.cursor()

    cursor.execute("SELECT id, company_name FROM companies ORDER BY company_name ASC")
    companies = cursor.fetchall()

    cursor.execute(
        """
        SELECT 
            subscriptions.id,
            companies.company_name,
            plans.plan_name
        FROM subscriptions
        JOIN companies ON subscriptions.company_id = companies.id
        JOIN plans ON subscriptions.plan_id = plans.id
        ORDER BY subscriptions.id DESC
        """
    )
    subscriptions = cursor.fetchall()

    cursor.close()

    return render_template(
        "invoices/invoice_create.html",
        companies=companies,
        subscriptions=subscriptions
    )


@invoice_bp.route("/invoice/<int:invoice_id>")
@login_required
@role_required(1, 2, 3)
def invoice_details(invoice_id):
    invoice = Invoice.get_by_id(invoice_id)
    return render_template("invoices/invoice_details.html", invoice=invoice)


@invoice_bp.route("/invoice/preview/<int:invoice_id>")
@login_required
@role_required(1, 2, 3)
def invoice_preview(invoice_id):
    invoice = Invoice.get_by_id(invoice_id)
    return render_template("invoices/invoice_preview.html", invoice=invoice)


@invoice_bp.route("/invoice/pdf/<int:invoice_id>")
@login_required
@role_required(1, 2, 3)
def invoice_pdf(invoice_id):
    invoice = Invoice.get_by_id(invoice_id)
    return render_template("invoices/invoice_pdf.html", invoice=invoice)


@invoice_bp.route("/invoice/update-status/<int:invoice_id>", methods=["POST"])
@login_required
@role_required(1, 3)
def invoice_update_status(invoice_id):
    status = request.form.get("status")
    invoice = Invoice.get_by_id(invoice_id)

    Invoice.update_status(invoice_id, status)

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
            Notification.create(
                user_id=user[0],
                title="Invoice Status Updated",
                message=f"Invoice {invoice_number} status has been updated to {status}."
            )

    flash("Invoice status updated successfully.", "success")
    return redirect(url_for("invoices.invoice_details", invoice_id=invoice_id))


@invoice_bp.route("/invoice/delete/<int:invoice_id>")
@login_required
@role_required(1, 3)
def invoice_delete(invoice_id):
    try:
        Invoice.delete(invoice_id)
        flash("Invoice deleted successfully.", "success")
    except Exception:
        flash("Cannot delete this invoice because payment records are linked to it.", "danger")

    return redirect(url_for("invoices.invoice_list"))