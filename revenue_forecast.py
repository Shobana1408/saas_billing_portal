import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def get_revenue_dataset_path():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "ai_models", "dataset", "revenue_data.csv")


def load_revenue_data():
    dataset_path = get_revenue_dataset_path()
    return pd.read_csv(dataset_path)


def forecast_revenue():
    data = load_revenue_data()

    x = np.array(range(len(data))).reshape(-1, 1)
    y = data["revenue"]

    model = LinearRegression()
    model.fit(x, y)

    next_month = np.array([[len(data)]])
    predicted_revenue = model.predict(next_month)[0]

    return round(float(predicted_revenue), 2)


def get_revenue_report_data():
    data = load_revenue_data()

    records = []

    for _, row in data.iterrows():
        records.append({
            "month": row["month"],
            "revenue": float(row["revenue"]),
            "expenses": float(row["expenses"]),
            "profit": float(row["profit"]),
            "active_subscriptions": int(row["active_subscriptions"]),
            "new_users": int(row["new_users"])
        })

    return records


def get_revenue_summary():
    data = load_revenue_data()

    total_revenue = float(data["revenue"].sum())
    total_expenses = float(data["expenses"].sum())
    total_profit = float(data["profit"].sum())
    average_revenue = float(data["revenue"].mean())
    latest_month = data.iloc[-1]["month"]
    latest_revenue = float(data.iloc[-1]["revenue"])

    predicted_revenue = forecast_revenue()

    growth_difference = predicted_revenue - latest_revenue
    growth_percentage = 0

    if latest_revenue > 0:
        growth_percentage = round((growth_difference / latest_revenue) * 100, 2)

    return {
        "total_revenue": round(total_revenue, 2),
        "total_expenses": round(total_expenses, 2),
        "total_profit": round(total_profit, 2),
        "average_revenue": round(average_revenue, 2),
        "latest_month": latest_month,
        "latest_revenue": round(latest_revenue, 2),
        "predicted_revenue": predicted_revenue,
        "growth_difference": round(growth_difference, 2),
        "growth_percentage": growth_percentage
    }


def get_chart_data():
    data = load_revenue_data()

    return {
        "months": data["month"].tolist(),
        "revenues": data["revenue"].astype(float).tolist(),
        "expenses": data["expenses"].astype(float).tolist(),
        "profits": data["profit"].astype(float).tolist(),
        "subscriptions": data["active_subscriptions"].astype(int).tolist(),
        "new_users": data["new_users"].astype(int).tolist()
    }


if __name__ == "__main__":
    print("Predicted Next Month Revenue:", forecast_revenue())