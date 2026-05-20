from flask import render_template
from flask_mail import Message
from app import mail


def send_email(subject, recipients, template_name, **kwargs):
    try:
        html_body = render_template(template_name, **kwargs)

        message = Message(
            subject=subject,
            recipients=recipients,
            html=html_body
        )

        mail.send(message)

        return {
            "status": True,
            "message": "Email sent successfully"
        }

    except Exception as error:
        return {
            "status": False,
            "message": str(error)
        }


def send_welcome_email(user_email, user_name, role_name):
    return send_email(
        subject="Welcome to SaaS Billing Portal",
        recipients=[user_email],
        template_name="emails/welcome_email.html",
        user_name=user_name,
        email=user_email,
        role_name=role_name
    )


def send_invoice_email(user_email, user_name, invoice_number, amount, tax, total_amount, due_date):
    return send_email(
        subject="Invoice Generated",
        recipients=[user_email],
        template_name="emails/invoice_generated.html",
        user_name=user_name,
        invoice_number=invoice_number,
        amount=amount,
        tax=tax,
        total_amount=total_amount,
        due_date=due_date
    )


def send_payment_success_email(user_email, user_name, invoice_number, transaction_id, amount_paid):
    return send_email(
        subject="Payment Successful",
        recipients=[user_email],
        template_name="emails/payment_success.html",
        user_name=user_name,
        invoice_number=invoice_number,
        transaction_id=transaction_id,
        amount_paid=amount_paid
    )


def send_payment_failed_email(user_email, user_name, invoice_number, amount):
    return send_email(
        subject="Payment Failed",
        recipients=[user_email],
        template_name="emails/payment_failed.html",
        user_name=user_name,
        invoice_number=invoice_number,
        amount=amount
    )