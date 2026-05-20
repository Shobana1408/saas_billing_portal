from models.analytics import Analytics


class AnalyticsService:

    @staticmethod
    def get_dashboard_summary():
        return {
            "total_revenue": Analytics.total_revenue(),
            "total_users": Analytics.total_users(),
            "total_companies": Analytics.total_companies(),
            "active_subscriptions": Analytics.active_subscriptions(),
            "failed_payments": Analytics.failed_payments()
        }

    @staticmethod
    def get_monthly_revenue():
        revenue_data = Analytics.monthly_revenue()

        months = []
        revenues = []

        for row in revenue_data:
            months.append(row[0])
            revenues.append(float(row[1]))

        return {
            "months": months,
            "revenues": revenues
        }

    @staticmethod
    def get_revenue_status():
        total_revenue = Analytics.total_revenue()

        if total_revenue >= 100000:
            return "Excellent revenue performance"
        elif total_revenue >= 50000:
            return "Good revenue performance"
        else:
            return "Revenue needs improvement"