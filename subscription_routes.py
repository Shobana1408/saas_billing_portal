from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from app import mysql
from models.plan import Plan
from models.subscription import Subscription
from utils.decorators import role_required

subscription_bp = Blueprint("subscriptions", __name__)


@subscription_bp.route("/plans")
@login_required
@role_required(1, 2)
def plans():
    plans = Plan.get_all()
    return render_template("subscriptions/plans.html", plans=plans)


@subscription_bp.route("/plans/create", methods=["GET", "POST"])
@login_required
@role_required(1)
def create_plan():
    if request.method == "POST":
        plan_name = request.form.get("plan_name")
        price = request.form.get("price")
        billing_cycle = request.form.get("billing_cycle")
        max_users = request.form.get("max_users")
        features = request.form.get("features")

        Plan.create(
            plan_name=plan_name,
            price=price,
            billing_cycle=billing_cycle,
            max_users=max_users,
            features=features
        )

        flash("Plan created successfully.", "success")
        return redirect(url_for("subscriptions.plans"))

    return render_template("subscriptions/plan_create.html")


@subscription_bp.route("/subscriptions")
@login_required
@role_required(1, 2)
def subscription_list():
    subscriptions = Subscription.get_all()

    summary = {
        "active": Subscription.total_active(),
        "cancelled": Subscription.total_cancelled(),
        "expired": Subscription.total_expired()
    }

    return render_template(
        "subscriptions/subscription_list.html",
        subscriptions=subscriptions,
        summary=summary
    )


@subscription_bp.route("/subscription/create", methods=["GET", "POST"])
@login_required
@role_required(1, 2)
def subscription_create():
    if request.method == "POST":
        company_id = request.form.get("company_id")
        plan_id = request.form.get("plan_id")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        status = request.form.get("status")
        auto_renew = True if request.form.get("auto_renew") else False

        Subscription.create(
            company_id=company_id,
            plan_id=plan_id,
            start_date=start_date,
            end_date=end_date,
            status=status,
            auto_renew=auto_renew
        )

        flash("Subscription created successfully.", "success")
        return redirect(url_for("subscriptions.subscription_list"))

    cursor = mysql.connection.cursor()

    cursor.execute("SELECT id, company_name FROM companies ORDER BY company_name ASC")
    companies = cursor.fetchall()

    cursor.execute("SELECT id, plan_name, price, billing_cycle FROM plans ORDER BY price ASC")
    plans = cursor.fetchall()

    cursor.close()

    return render_template(
        "subscriptions/subscription_create.html",
        companies=companies,
        plans=plans
    )


@subscription_bp.route("/subscription/<int:subscription_id>")
@login_required
@role_required(1, 2)
def subscription_details(subscription_id):
    subscription = Subscription.get_by_id(subscription_id)
    return render_template("subscriptions/subscription_details.html", subscription=subscription)


@subscription_bp.route("/subscription/edit/<int:subscription_id>", methods=["GET", "POST"])
@login_required
@role_required(1, 2)
def subscription_edit(subscription_id):
    subscription = Subscription.get_by_id(subscription_id)

    if request.method == "POST":
        plan_id = request.form.get("plan_id")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        status = request.form.get("status")
        auto_renew = True if request.form.get("auto_renew") else False

        Subscription.update(
            subscription_id=subscription_id,
            plan_id=plan_id,
            start_date=start_date,
            end_date=end_date,
            status=status,
            auto_renew=auto_renew
        )

        flash("Subscription updated successfully.", "success")
        return redirect(url_for("subscriptions.subscription_details", subscription_id=subscription_id))

    plans = Plan.get_all()

    return render_template(
        "subscriptions/subscription_edit.html",
        subscription=subscription,
        plans=plans
    )


@subscription_bp.route("/subscription/cancel/<int:subscription_id>")
@login_required
@role_required(1, 2)
def subscription_cancel(subscription_id):
    Subscription.cancel(subscription_id)

    flash("Subscription cancelled successfully.", "success")
    return redirect(url_for("subscriptions.subscription_list"))


@subscription_bp.route("/subscription/activate/<int:subscription_id>")
@login_required
@role_required(1, 2)
def subscription_activate(subscription_id):
    Subscription.activate(subscription_id)

    flash("Subscription activated successfully.", "success")
    return redirect(url_for("subscriptions.subscription_list"))


@subscription_bp.route("/subscription/upgrade/<int:subscription_id>", methods=["GET", "POST"])
@login_required
@role_required(1, 2)
def upgrade_plan(subscription_id):
    subscription = Subscription.get_by_id(subscription_id)

    if request.method == "POST":
        plan_id = request.form.get("plan_id")

        Subscription.upgrade_plan(subscription_id, plan_id)

        flash("Plan upgraded successfully.", "success")
        return redirect(url_for("subscriptions.subscription_details", subscription_id=subscription_id))

    plans = Plan.get_all()

    return render_template(
        "subscriptions/upgrade_plan.html",
        subscription=subscription,
        plans=plans
    )