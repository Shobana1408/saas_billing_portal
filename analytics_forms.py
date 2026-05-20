from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Optional


class RevenueReportForm(FlaskForm):
    start_date = DateField(
        "Start Date",
        format="%Y-%m-%d",
        validators=[
            Optional()
        ]
    )

    end_date = DateField(
        "End Date",
        format="%Y-%m-%d",
        validators=[
            Optional()
        ]
    )

    report_type = SelectField(
        "Report Type",
        choices=[
            ("monthly", "Monthly"),
            ("quarterly", "Quarterly"),
            ("yearly", "Yearly")
        ],
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Generate Report")


class ForecastForm(FlaskForm):
    forecast_period = SelectField(
        "Forecast Period",
        choices=[
            ("next_month", "Next Month"),
            ("next_quarter", "Next Quarter"),
            ("next_year", "Next Year")
        ],
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Generate Forecast")


class ChurnReportForm(FlaskForm):
    risk_level = SelectField(
        "Risk Level",
        choices=[
            ("all", "All"),
            ("low", "Low"),
            ("medium", "Medium"),
            ("high", "High")
        ],
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("View Churn Report")


class AnalyticsFilterForm(FlaskForm):
    company_id = SelectField(
        "Company",
        coerce=int,
        validators=[
            Optional()
        ]
    )

    month = SelectField(
        "Month",
        choices=[
            ("all", "All"),
            ("January", "January"),
            ("February", "February"),
            ("March", "March"),
            ("April", "April"),
            ("May", "May"),
            ("June", "June"),
            ("July", "July"),
            ("August", "August"),
            ("September", "September"),
            ("October", "October"),
            ("November", "November"),
            ("December", "December")
        ],
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Apply Filter")