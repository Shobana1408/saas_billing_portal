from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, DecimalField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length


class InvoiceForm(FlaskForm):
    company_id = SelectField(
        "Company",
        coerce=int,
        validators=[
            DataRequired()
        ]
    )

    subscription_id = SelectField(
        "Subscription",
        coerce=int,
        validators=[
            DataRequired()
        ]
    )

    invoice_number = StringField(
        "Invoice Number",
        validators=[
            DataRequired(),
            Length(min=3, max=100)
        ]
    )

    amount = DecimalField(
        "Amount",
        places=2,
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ]
    )

    tax = DecimalField(
        "Tax",
        places=2,
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ]
    )

    total_amount = DecimalField(
        "Total Amount",
        places=2,
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ]
    )

    due_date = DateField(
        "Due Date",
        format="%Y-%m-%d",
        validators=[
            DataRequired()
        ]
    )

    status = SelectField(
        "Status",
        choices=[
            ("paid", "Paid"),
            ("unpaid", "Unpaid"),
            ("overdue", "Overdue")
        ],
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Save Invoice")


class InvoiceStatusForm(FlaskForm):
    status = SelectField(
        "Invoice Status",
        choices=[
            ("paid", "Paid"),
            ("unpaid", "Unpaid"),
            ("overdue", "Overdue")
        ],
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Update Status")


class InvoiceSearchForm(FlaskForm):
    invoice_number = StringField(
        "Invoice Number",
        validators=[
            Length(max=100)
        ]
    )

    status = SelectField(
        "Status",
        choices=[
            ("all", "All"),
            ("paid", "Paid"),
            ("unpaid", "Unpaid"),
            ("overdue", "Overdue")
        ]
    )

    submit = SubmitField("Search")