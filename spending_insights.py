import os
import pandas as pd


def get_billing_dataset_path():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "ai_models", "dataset", "billing_data.csv")


def load_billing_data():
    dataset_path = get_billing_dataset_path()
    return pd.read_csv(dataset_path)


def generate_spending_insights():
    data = load_billing_data()

    insights = []
    average_cost = float(data["monthly_cost"].mean())
    average_failed_payments = float(data["payments_failed"].mean())

    for _, row in data.iterrows():
        company_name = row["company_name"]
        monthly_cost = float(row["monthly_cost"])
        failed_payments = int(row["payments_failed"])
        plan = row["subscription_plan"]

        if monthly_cost > average_cost:
            insights.append({
                "type": "Cost Alert",
                "company": company_name,
                "message": f"{company_name} is spending above average with ₹{monthly_cost}.",
                "recommendation": "Review plan usage and optimize subscription allocation.",
                "severity": "Medium"
            })

        if failed_payments > average_failed_payments:
            insights.append({
                "type": "Payment Risk",
                "company": company_name,
                "message": f"{company_name} has {failed_payments} failed payments this period.",
                "recommendation": "Send payment reminders and verify payment method.",
                "severity": "High"
            })

        if plan == "Enterprise":
            insights.append({
                "type": "Enterprise Account",
                "company": company_name,
                "message": f"{company_name} is on Enterprise plan.",
                "recommendation": "Prioritize customer success and renewal follow-up.",
                "severity": "Low"
            })

    return insights


def get_spending_summary():
    data = load_billing_data()

    total_cost = float(data["monthly_cost"].sum())
    average_cost = float(data["monthly_cost"].mean())
    successful_payments = int(data["payments_successful"].sum())
    failed_payments = int(data["payments_failed"].sum())
    total_users = int(data["total_users"].sum())

    return {
        "total_cost": round(total_cost, 2),
        "average_cost": round(average_cost, 2),
        "successful_payments": successful_payments,
        "failed_payments": failed_payments,
        "total_users": total_users,
        "total_companies": len(data)
    }


def get_billing_records():
    data = load_billing_data()

    records = []

    for _, row in data.iterrows():
        records.append({
            "billing_id": int(row["billing_id"]),
            "company_name": row["company_name"],
            "month": row["month"],
            "total_users": int(row["total_users"]),
            "subscription_plan": row["subscription_plan"],
            "monthly_cost": float(row["monthly_cost"]),
            "payments_successful": int(row["payments_successful"]),
            "payments_failed": int(row["payments_failed"])
        })

    return records


if __name__ == "__main__":
    print(generate_spending_insights())