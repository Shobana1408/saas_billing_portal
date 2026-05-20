from revenue_forecast import forecast_revenue
from churn_prediction import predict_churn_risk
from spending_insights import generate_spending_insights


def run_all_predictions():

    revenue = forecast_revenue()
    churn = predict_churn_risk()
    spending = generate_spending_insights()

    print("\n========== AI ANALYTICS REPORT ==========\n")

    print(f"Predicted Revenue Next Month: ₹{revenue}\n")

    print("High Churn Risk Companies:")

    for company in churn:
        print(f"- {company['company']} ({company['churn_rate']}%)")

    print("\nSpending Insights:")

    for insight in spending:
        print(f"- {insight}")

    print("\n=========================================\n")


if __name__ == "__main__":
    run_all_predictions()