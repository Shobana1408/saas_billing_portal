from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash

from app import mysql
from models.user import User
from utils.decorators import role_required

user_bp = Blueprint("users", __name__)


@user_bp.route("/users")
@login_required
@role_required(1, 2)
def user_list():
    users = User.get_all()
    return render_template("users/user_list.html", users=users)


@user_bp.route("/users/<int:user_id>")
@login_required
@role_required(1, 2)
def user_details(user_id):
    user = User.get_details_by_id(user_id)
    return render_template("users/user_details.html", user=user)


@user_bp.route("/users/create", methods=["GET", "POST"])
@login_required
@role_required(1, 2)
def create_user():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")
        role_id = request.form.get("role_id")
        company_id = request.form.get("company_id")
        status = request.form.get("status")

        existing_user = User.get_by_email(email)

        if existing_user:
            flash("Email already exists. Please use another email.", "warning")
            return redirect(url_for("users.create_user"))

        hashed_password = generate_password_hash(password)

        User.create(
            full_name=full_name,
            email=email,
            password=hashed_password,
            role_id=role_id,
            company_id=company_id,
            status=status
        )

        flash("User created successfully.", "success")
        return redirect(url_for("users.user_list"))

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, role_name FROM roles")
    roles = cursor.fetchall()

    cursor.execute("SELECT id, company_name FROM companies")
    companies = cursor.fetchall()
    cursor.close()

    return render_template("users/user_create.html", roles=roles, companies=companies)


@user_bp.route("/users/update-status/<int:user_id>", methods=["POST"])
@login_required
@role_required(1, 2)
def update_user_status(user_id):
    status = request.form.get("status")
    User.update_status(user_id, status)

    flash("User status updated successfully.", "success")
    return redirect(url_for("users.user_details", user_id=user_id))


@user_bp.route("/profile")
@login_required
def profile():
    user = User.get_details_by_id(current_user.id)
    return render_template("users/profile.html", user=user)


@user_bp.route("/edit-profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")

        existing_user = User.get_by_email(email)

        if existing_user and int(existing_user.id) != int(current_user.id):
            flash("This email is already used by another account.", "warning")
            return redirect(url_for("users.edit_profile"))

        User.update_profile(current_user.id, full_name, email)

        flash("Profile updated successfully. Please refresh or login again to see all changes.", "success")
        return redirect(url_for("users.profile"))

    user = User.get_details_by_id(current_user.id)
    return render_template("users/edit_profile.html", user=user)


@user_bp.route("/role-assign", methods=["GET", "POST"])
@login_required
@role_required(1)
def role_assign():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        role_id = request.form.get("role_id")

        User.update_role(user_id, role_id)

        flash("Role assigned successfully.", "success")
        return redirect(url_for("users.user_list"))

    users = User.get_all()

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, role_name FROM roles")
    roles = cursor.fetchall()
    cursor.close()

    return render_template("users/role_assign.html", users=users, roles=roles)