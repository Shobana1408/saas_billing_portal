from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class RoleForm(FlaskForm):
    role_name = StringField(
        "Role Name",
        validators=[
            DataRequired(),
            Length(min=2, max=50)
        ]
    )

    description = TextAreaField(
        "Description",
        validators=[
            Optional(),
            Length(max=500)
        ]
    )

    submit = SubmitField("Save Role")


class SystemSettingsForm(FlaskForm):
    site_name = StringField(
        "Site Name",
        validators=[
            DataRequired(),
            Length(min=3, max=100)
        ]
    )

    admin_email = StringField(
        "Admin Email",
        validators=[
            DataRequired(),
            Length(max=120)
        ]
    )

    default_currency = SelectField(
        "Default Currency",
        choices=[
            ("INR", "Indian Rupee"),
            ("USD", "US Dollar"),
            ("EUR", "Euro")
        ],
        validators=[
            DataRequired()
        ]
    )

    maintenance_mode = SelectField(
        "Maintenance Mode",
        choices=[
            ("off", "Off"),
            ("on", "On")
        ],
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Save Settings")


class AuditLogFilterForm(FlaskForm):
    user_id = SelectField(
        "User",
        coerce=int,
        validators=[
            Optional()
        ]
    )

    action_type = StringField(
        "Action Type",
        validators=[
            Optional(),
            Length(max=100)
        ]
    )

    submit = SubmitField("Filter Logs")


class AdminSearchForm(FlaskForm):
    keyword = StringField(
        "Search",
        validators=[
            Optional(),
            Length(max=100)
        ]
    )

    submit = SubmitField("Search")