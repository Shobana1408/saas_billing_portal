from utils.decorators import role_required
from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.analytics import Analytics
from models.role import Role

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    role_name = Role.get_role_name(current_user.role_id)

    total_revenue = Analytics.total_revenue()
    total_users = Analytics.total_users()
    total_companies = Analytics.total_companies()
    active_subscriptions = Analytics.active_subscriptions()
    failed_payments = Analytics.failed_payments()

    data = {
        "total_revenue": total_revenue,
        "total_users": total_users,
        "total_companies": total_companies,
        "active_subscriptions": active_subscriptions,
        "failed_payments": failed_payments
    }

    if role_name == "Super Admin":
        return render_template("dashboard/admin_dashboard.html", data=data)

    elif role_name == "Company Admin":
        return render_template("dashboard/company_dashboard.html", data=data)

    elif role_name == "Finance Manager":
        return render_template("dashboard/finance_dashboard.html", data=data)

    else:
        return render_template("dashboard/user_dashboard.html", data=data)