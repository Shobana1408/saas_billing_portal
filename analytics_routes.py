from flask import Blueprint, render_template, jsonify
from flask_login import login_required

from models.analytics import Analytics
from ai_models.revenue_forecast import (
    forecast_revenue,
    get_revenue_report_data,
    get_revenue_summary,
    get_chart_data
)
from ai_models.churn_prediction import (
    predict_churn_risk,
    get_churn_summary,
    get_high_risk_companies
)
from ai_models.spending_insights import (
    generate_spending_insights,
    get_spending_summary,
    get_billing_records
)
from utils.decorators import role_required

analytics_bp = Blueprint("analytics", __name__)


@analytics_bp.route("/analytics")
@login_required
@role_required(1, 2, 3)
def analytics_home():
    revenue_summary = get_revenue_summary()
    churn_summary = get_churn_summary()
    spending_summary = get_spending_summary()

    return render_template(
        "analytics/analytics_home.html",
        revenue_summary=revenue_summary,
        churn_summary=churn_summary,
        spending_summary=spending_summary
    )


@analytics_bp.route("/analytics/revenue-report")
@login_required
@role_required(1, 2, 3)
def revenue_report():
    revenue_records = get_revenue_report_data()
    revenue_summary = get_revenue_summary()
    chart_data = get_chart_data()

    return render_template(
        "analytics/revenue_report.html",
        revenue_records=revenue_records,
        revenue_summary=revenue_summary,
        chart_data=chart_data
    )


@analytics_bp.route("/analytics/user-growth")
@login_required
@role_required(1, 2, 3)
def user_growth():
    chart_data = get_chart_data()

    return render_template(
        "analytics/user_growth.html",
        chart_data=chart_data
    )


@analytics_bp.route("/analytics/churn-report")
@login_required
@role_required(1, 2, 3)
def churn_report():
    churn_data = predict_churn_risk()
    churn_summary = get_churn_summary()

    return render_template(
        "analytics/churn_report.html",
        churn_data=churn_data,
        churn_summary=churn_summary
    )


@analytics_bp.route("/analytics/forecast")
@login_required
@role_required(1, 2, 3)
def forecast():
    revenue_summary = get_revenue_summary()
    chart_data = get_chart_data()

    return render_template(
        "analytics/forecast.html",
        revenue_summary=revenue_summary,
        chart_data=chart_data
    )


@analytics_bp.route("/analytics/ai-insights")
@login_required
@role_required(1, 2, 3)
def ai_insights():
    revenue_summary = get_revenue_summary()
    churn_summary = get_churn_summary()
    high_risk_companies = get_high_risk_companies()
    spending_summary = get_spending_summary()
    spending_insights = generate_spending_insights()
    billing_records = get_billing_records()

    return render_template(
        "analytics/ai_insights.html",
        revenue_summary=revenue_summary,
        churn_summary=churn_summary,
        high_risk_companies=high_risk_companies,
        spending_summary=spending_summary,
        spending_insights=spending_insights,
        billing_records=billing_records
    )


@analytics_bp.route("/analytics/revenue-forecast")
@login_required
@role_required(1, 2, 3)
def revenue_forecast_api():
    return jsonify({
        "predicted_revenue": forecast_revenue()
    })


@analytics_bp.route("/analytics/churn-prediction")
@login_required
@role_required(1, 2, 3)
def churn_prediction_api():
    return jsonify(predict_churn_risk())


@analytics_bp.route("/analytics/spending-insights")
@login_required
@role_required(1, 2, 3)
def spending_insights_api():
    return jsonify(generate_spending_insights())