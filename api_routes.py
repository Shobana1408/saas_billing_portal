from utils.decorators import role_required
from flask import Blueprint, jsonify
from flask_login import login_required

from models.analytics import Analytics
from models.user import User
from models.company import Company
from models.plan import Plan
from models.subscription import Subscription
from models.invoice import Invoice
from models.payment import Payment
from ai_models.revenue_forecast import forecast_revenue
from ai_models.churn_prediction import predict_churn_risk
from ai_models.spending_insights import generate_spending_insights

api_bp = Blueprint("api", __name__)


@api_bp.route("/api/dashboard-summary")
@login_required
def dashboard_summary():
    return jsonify({
        "total_revenue": Analytics.total_revenue(),
        "total_users": Analytics.total_users(),
        "total_companies": Analytics.total_companies(),
        "active_subscriptions": Analytics.active_subscriptions(),
        "failed_payments": Analytics.failed_payments()
    })


@api_bp.route("/api/users")
@login_required
def api_users():
    users = User.get_all()
    return jsonify(users)


@api_bp.route("/api/companies")
@login_required
def api_companies():
    companies = Company.get_all()
    return jsonify(companies)


@api_bp.route("/api/plans")
@login_required
def api_plans():
    plans = Plan.get_all()
    return jsonify(plans)


@api_bp.route("/api/subscriptions")
@login_required
def api_subscriptions():
    subscriptions = Subscription.get_all()
    return jsonify(subscriptions)


@api_bp.route("/api/invoices")
@login_required
def api_invoices():
    invoices = Invoice.get_all()
    return jsonify(invoices)


@api_bp.route("/api/payments")
@login_required
def api_payments():
    payments = Payment.get_all()
    return jsonify(payments)


@api_bp.route("/api/revenue-forecast")
@login_required
def api_revenue_forecast():
    return jsonify({
        "predicted_revenue": forecast_revenue()
    })


@api_bp.route("/api/churn-prediction")
@login_required
def api_churn_prediction():
    return jsonify(predict_churn_risk())


@api_bp.route("/api/spending-insights")
@login_required
def api_spending_insights():
    return jsonify(generate_spending_insights())