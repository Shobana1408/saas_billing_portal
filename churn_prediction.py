import os
import pandas as pd


def get_churn_dataset_path():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "ai_models", "dataset", "churn_data.csv")


def load_churn_data():
    dataset_path = get_churn_dataset_path()
    return pd.read_csv(dataset_path)


def get_risk_level(churn_rate):
    churn_rate = float(churn_rate)

    if churn_rate >= 15:
        return "High"
    elif churn_rate >= 8:
        return "Medium"
    else:
        return "Low"


def predict_churn_risk():
    data = load_churn_data()

    companies = []

    for _, row in data.iterrows():
        churn_rate = float(row["churn_rate"])

        companies.append({
            "company": row["company_name"],
            "total_users": int(row["total_users"]),
            "cancelled_users": int(row["cancelled_users"]),
            "churn_rate": churn_rate,
            "risk_level": get_risk_level(churn_rate),
            "subscription_plan": row["subscription_plan"],
            "monthly_revenue": float(row["monthly_revenue"])
        })

    companies.sort(key=lambda item: item["churn_rate"], reverse=True)

    return companies


def get_high_risk_companies():
    companies = predict_churn_risk()
    return [company for company in companies if company["risk_level"] == "High"]


def get_churn_summary():
    data = load_churn_data()

    total_users = int(data["total_users"].sum())
    total_cancelled = int(data["cancelled_users"].sum())
    average_churn = round(float(data["churn_rate"].mean()), 2)

    high_risk = 0
    medium_risk = 0
    low_risk = 0

    for _, row in data.iterrows():
        risk = get_risk_level(row["churn_rate"])

        if risk == "High":
            high_risk += 1
        elif risk == "Medium":
            medium_risk += 1
        else:
            low_risk += 1

    return {
        "total_users": total_users,
        "total_cancelled": total_cancelled,
        "average_churn": average_churn,
        "high_risk": high_risk,
        "medium_risk": medium_risk,
        "low_risk": low_risk,
        "total_companies": len(data)
    }


if __name__ == "__main__":
    print(predict_churn_risk())