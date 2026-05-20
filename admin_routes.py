from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from models.role import Role
from models.plan import Plan
from models.audit_log import AuditLog
from utils.decorators import role_required

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin")
@login_required
@role_required(1)
def admin_home():
    return render_template("admin/admin_home.html")


@admin_bp.route("/admin/roles")
@login_required
@role_required(1)
def manage_roles():
    roles = Role.get_all()
    return render_template("admin/manage_roles.html", roles=roles)


@admin_bp.route("/admin/roles/create", methods=["POST"])
@login_required
@role_required(1)
def create_role():
    role_name = request.form.get("role_name")
    description = request.form.get("description")

    Role.create(role_name, description)

    flash("Role created successfully.", "success")
    return redirect(url_for("admin.manage_roles"))


@admin_bp.route("/admin/plans")
@login_required
@role_required(1)
def manage_plans():
    plans = Plan.get_all()
    return render_template("admin/manage_plans.html", plans=plans)


@admin_bp.route("/admin/system-logs")
@login_required
@role_required(1)
def system_logs():
    return render_template("admin/system_logs.html")


@admin_bp.route("/admin/audit-logs")
@login_required
@role_required(1)
def audit_logs():
    logs = AuditLog.get_all()
    return render_template("admin/audit_logs.html", logs=logs)


@admin_bp.route("/admin/settings", methods=["GET", "POST"])
@login_required
@role_required(1)
def settings():
    if request.method == "POST":
        flash("Settings updated successfully.", "success")
        return redirect(url_for("admin.settings"))

    return render_template("admin/settings.html")