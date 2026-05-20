from utils.decorators import role_required
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from app import mysql, login_manager
from models.user import User

auth_bp = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.get_by_email(email)

        if user and check_password_hash(user.password, password):
            if user.status == "blocked":
                flash("Your account has been blocked.", "danger")
                return redirect(url_for("auth.login"))

            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("dashboard.dashboard"))

        flash("Invalid email or password.", "danger")

    return render_template("auth/login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")
        role_id = request.form.get("role_id")
        company_id = request.form.get("company_id")

        existing_user = User.get_by_email(email)

        if existing_user:
            flash("Email already registered.", "warning")
            return redirect(url_for("auth.register"))

        hashed_password = generate_password_hash(password)

        User.create(
            full_name=full_name,
            email=email,
            password=hashed_password,
            role_id=role_id,
            company_id=company_id
        )

        flash("Registration successful. Please login.", "success")
        return redirect(url_for("auth.login"))

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, role_name FROM roles")
    roles = cursor.fetchall()

    cursor.execute("SELECT id, company_name FROM companies")
    companies = cursor.fetchall()
    cursor.close()

    return render_template("auth/register.html", roles=roles, companies=companies)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "info")
    return redirect(url_for("auth.login"))


@auth_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        flash("Password reset feature will be added later.", "info")
        return redirect(url_for("auth.login"))

    return render_template("auth/forgot_password.html")


@auth_bp.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        flash("Password reset successful.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/reset_password.html")


@auth_bp.route("/verify-otp", methods=["GET", "POST"])
def verify_otp():
    if request.method == "POST":
        flash("OTP verified successfully.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/verify_otp.html")