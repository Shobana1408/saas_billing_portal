from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional, EqualTo


class UserCreateForm(FlaskForm):
    full_name = StringField(
        "Full Name",
        validators=[
            DataRequired(),
            Length(min=3, max=100)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    role_id = SelectField(
        "Role",
        coerce=int,
        validators=[
            DataRequired()
        ]
    )

    company_id = SelectField(
        "Company",
        coerce=int,
        validators=[
            Optional()
        ]
    )

    status = SelectField(
        "Status",
        choices=[
            ("active", "Active"),
            ("inactive", "Inactive"),
            ("blocked", "Blocked")
        ],
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Create User")


class UserEditForm(FlaskForm):
    full_name = StringField(
        "Full Name",
        validators=[
            DataRequired(),
            Length(min=3, max=100)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    role_id = SelectField(
        "Role",
        coerce=int,
        validators=[
            DataRequired()
        ]
    )

    company_id = SelectField(
        "Company",
        coerce=int,
        validators=[
            Optional()
        ]
    )

    status = SelectField(
        "Status",
        choices=[
            ("active", "Active"),
            ("inactive", "Inactive"),
            ("blocked", "Blocked")
        ],
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Update User")


class ProfileUpdateForm(FlaskForm):
    full_name = StringField(
        "Full Name",
        validators=[
            DataRequired(),
            Length(min=3, max=100)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    profile_image = FileField(
        "Profile Image",
        validators=[
            FileAllowed(["jpg", "jpeg", "png"], "Only image files are allowed")
        ]
    )

    submit = SubmitField("Update Profile")


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField(
        "Current Password",
        validators=[
            DataRequired()
        ]
    )

    new_password = PasswordField(
        "New Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    confirm_password = PasswordField(
        "Confirm New Password",
        validators=[
            DataRequired(),
            EqualTo("new_password", message="Passwords must match")
        ]
    )

    submit = SubmitField("Change Password")


class RoleAssignForm(FlaskForm):
    role_id = SelectField(
        "Select Role",
        coerce=int,
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Assign Role")