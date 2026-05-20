from ai_models.revenue_forecast import forecast_revenue
from ai_models.churn_prediction import predict_churn_risk
from ai_models.spending_insights import generate_spending_insights
from models.ai_prediction import AIPrediction


class AIService:

    @staticmethod
    def get_revenue_forecast():
        predicted_revenue = forecast_revenue()

        AIPrediction.create(
            prediction_type="Revenue Forecast",
            prediction_result=f"Predicted next month revenue is ₹{predicted_revenue}"
        )

        return predicted_revenue

    @staticmethod
    def get_churn_prediction():
        churn_data = predict_churn_risk()

        AIPrediction.create(
            prediction_type="Churn Prediction",
            prediction_result=str(churn_data)
        )

        return churn_data

    @staticmethod
    def get_spending_insights():
        insights = generate_spending_insights()

        AIPrediction.create(
            prediction_type="Spending Insights",
            prediction_result=str(insights)
        )

        return insights

    @staticmethod
    def get_all_ai_insights():
        return {
            "predicted_revenue": AIService.get_revenue_forecast(),
            "churn_risk": AIService.get_churn_prediction(),
            "spending_insights": AIService.get_spending_insights()
        }