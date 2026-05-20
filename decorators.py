from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user


def role_required(*allowed_roles):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                flash("Please login first.", "warning")
                return redirect(url_for("auth.login"))

            if int(current_user.role_id) not in allowed_roles:
                flash("You do not have permission to access this page.", "danger")
                return redirect(url_for("dashboard.dashboard"))

            return function(*args, **kwargs)

        return wrapper

    return decorator


def active_user_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Please login first.", "warning")
            return redirect(url_for("auth.login"))

        if current_user.status != "active":
            flash("Your account is not active.", "danger")
            return redirect(url_for("auth.logout"))

        return function(*args, **kwargs)

    return wrapper