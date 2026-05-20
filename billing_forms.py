from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired, Optional, NumberRange, Length


class PaymentForm(FlaskForm):
    invoice_id = SelectField(
        "Invoice",
        coerce=int,
        validators=[
            DataRequired()
        ]
    )

    payment_method = SelectField(
        "Payment Method",
        choices=[
            ("UPI", "UPI"),
            ("Credit Card", "Credit Card"),
            ("Debit Card", "Debit Card"),
            ("Net Banking", "Net Banking"),
            ("Cash", "Cash")
        ],
        validators=[
            DataRequired()
        ]
    )

    payment_status = SelectField(
        "Payment Status",
        choices=[
            ("success", "Success"),
            ("failed", "Failed"),
            ("pending", "Pending")
        ],
        validators=[
            DataRequired()
        ]
    )

    transaction_id = StringField(
        "Transaction ID",
        validators=[
            Optional(),
            Length(max=150)
        ]
    )

    amount_paid = DecimalField(
        "Amount Paid",
        places=2,
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ]
    )

    submit = SubmitField("Save Payment")


class BillingSettingsForm(FlaskForm):
    tax_percentage = DecimalField(
        "Tax Percentage",
        places=2,
        validators=[
            DataRequired(),
            NumberRange(min=0, max=100)
        ]
    )

    currency = SelectField(
        "Currency",
        choices=[
            ("INR", "Indian Rupee"),
            ("USD", "US Dollar"),
            ("EUR", "Euro")
        ],
        validators=[
            DataRequired()
        ]
    )

    billing_email = StringField(
        "Billing Email",
        validators=[
            Optional(),
            Length(max=120)
        ]
    )

    submit = SubmitField("Save Billing Settings")


class PaymentSearchForm(FlaskForm):
    payment_status = SelectField(
        "Payment Status",
        choices=[
            ("all", "All"),
            ("success", "Success"),
            ("failed", "Failed"),
            ("pending", "Pending")
        ],
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Filter")