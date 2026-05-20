from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, IntegerField
from wtforms import SelectField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class PlanForm(FlaskForm):
    plan_name = StringField(
        "Plan Name",
        validators=[
            DataRequired(),
            Length(min=2, max=50)
        ]
    )

    price = DecimalField(
        "Price",
        places=2,
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ]
    )

    billing_cycle = SelectField(
        "Billing Cycle",
        choices=[
            ("monthly", "Monthly"),
            ("yearly", "Yearly")
        ],
        validators=[
            DataRequired()
        ]
    )

    max_users = IntegerField(
        "Maximum Users",
        validators=[
            DataRequired(),
            NumberRange(min=1)
        ]
    )

    features = TextAreaField(
        "Features",
        validators=[
            Optional(),
            Length(max=1000)
        ]
    )

    submit = SubmitField("Save Plan")


class SubscriptionForm(FlaskForm):
    company_id = SelectField(
        "Company",
        coerce=int,
        validators=[
            DataRequired()
        ]
    )

    plan_id = SelectField(
        "Plan",
        coerce=int,
        validators=[
            DataRequired()
        ]
    )

    start_date = DateField(
        "Start Date",
        format="%Y-%m-%d",
        validators=[
            DataRequired()
        ]
    )

    end_date = DateField(
        "End Date",
        format="%Y-%m-%d",
        validators=[
            DataRequired()
        ]
    )

    status = SelectField(
        "Status",
        choices=[
            ("active", "Active"),
            ("expired", "Expired"),
            ("cancelled", "Cancelled")
        ],
        validators=[
            DataRequired()
        ]
    )

    auto_renew = BooleanField("Auto Renew")

    submit = SubmitField("Save Subscription")


class UpgradePlanForm(FlaskForm):
    plan_id = SelectField(
        "Select New Plan",
        coerce=int,
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Upgrade Plan")