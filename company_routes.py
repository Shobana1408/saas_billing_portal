from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from models.company import Company
from utils.decorators import role_required

company_bp = Blueprint("companies", __name__)


@company_bp.route("/companies")
@login_required
@role_required(1)
def company_list():
    companies = Company.get_all()
    return render_template("companies/company_list.html", companies=companies)


@company_bp.route("/company/create", methods=["GET", "POST"])
@login_required
@role_required(1)
def company_create():
    if request.method == "POST":
        company_name = request.form.get("company_name")
        company_email = request.form.get("company_email")
        company_phone = request.form.get("company_phone")
        company_address = request.form.get("company_address")
        industry = request.form.get("industry")
        total_employees = request.form.get("total_employees")

        if not total_employees:
            total_employees = 0

        Company.create(
            company_name=company_name,
            company_email=company_email,
            company_phone=company_phone,
            company_address=company_address,
            industry=industry,
            total_employees=total_employees
        )

        flash("Company created successfully.", "success")
        return redirect(url_for("companies.company_list"))

    return render_template("companies/company_create.html")


@company_bp.route("/company/<int:company_id>")
@login_required
@role_required(1)
def company_details(company_id):
    company = Company.get_by_id(company_id)
    summary = Company.get_company_summary(company_id)

    return render_template(
        "companies/company_details.html",
        company=company,
        summary=summary
    )


@company_bp.route("/company/edit/<int:company_id>", methods=["GET", "POST"])
@login_required
@role_required(1)
def company_edit(company_id):
    company = Company.get_by_id(company_id)

    if request.method == "POST":
        company_name = request.form.get("company_name")
        company_email = request.form.get("company_email")
        company_phone = request.form.get("company_phone")
        company_address = request.form.get("company_address")
        industry = request.form.get("industry")
        total_employees = request.form.get("total_employees")

        if not total_employees:
            total_employees = 0

        Company.update(
            company_id=company_id,
            company_name=company_name,
            company_email=company_email,
            company_phone=company_phone,
            company_address=company_address,
            industry=industry,
            total_employees=total_employees
        )

        flash("Company updated successfully.", "success")
        return redirect(url_for("companies.company_details", company_id=company_id))

    return render_template("companies/company_edit.html", company=company)


@company_bp.route("/company/delete/<int:company_id>")
@login_required
@role_required(1)
def company_delete(company_id):
    try:
        Company.delete(company_id)
        flash("Company deleted successfully.", "success")
    except Exception:
        flash("Cannot delete this company because it is linked with users, subscriptions, or invoices.", "danger")

    return redirect(url_for("companies.company_list"))