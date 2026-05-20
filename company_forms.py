from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange


class CompanyForm(FlaskForm):
    company_name = StringField(
        "Company Name",
        validators=[
            DataRequired(),
            Length(min=2, max=150)
        ]
    )

    company_email = StringField(
        "Company Email",
        validators=[
            Optional(),
            Email()
        ]
    )

    company_phone = StringField(
        "Company Phone",
        validators=[
            Optional(),
            Length(min=10, max=20)
        ]
    )

    company_address = TextAreaField(
        "Company Address",
        validators=[
            Optional(),
            Length(max=500)
        ]
    )

    industry = StringField(
        "Industry",
        validators=[
            Optional(),
            Length(max=100)
        ]
    )

    total_employees = IntegerField(
        "Total Employees",
        validators=[
            Optional(),
            NumberRange(min=0)
        ]
    )

    submit = SubmitField("Save Company")


class CompanySearchForm(FlaskForm):
    keyword = StringField(
        "Search Company",
        validators=[
            Optional(),
            Length(max=100)
        ]
    )

    submit = SubmitField("Search")