from models.subscription import Subscription
from models.plan import Plan


class SubscriptionService:

    @staticmethod
    def create_subscription(company_id, plan_id, start_date, end_date, status="active", auto_renew=True):
        Subscription.create(
            company_id=company_id,
            plan_id=plan_id,
            start_date=start_date,
            end_date=end_date,
            status=status,
            auto_renew=auto_renew
        )

        return {
            "status": True,
            "message": "Subscription created successfully"
        }

    @staticmethod
    def get_all_subscriptions():
        return Subscription.get_all()

    @staticmethod
    def get_subscription_details(subscription_id):
        return Subscription.get_by_id(subscription_id)

    @staticmethod
    def update_subscription(subscription_id, plan_id, start_date, end_date, status, auto_renew):
        Subscription.update(
            subscription_id=subscription_id,
            plan_id=plan_id,
            start_date=start_date,
            end_date=end_date,
            status=status,
            auto_renew=auto_renew
        )

        return {
            "status": True,
            "message": "Subscription updated successfully"
        }

    @staticmethod
    def cancel_subscription(subscription_id):
        Subscription.cancel(subscription_id)

        return {
            "status": True,
            "message": "Subscription cancelled successfully"
        }

    @staticmethod
    def get_all_plans():
        return Plan.get_all()

    @staticmethod
    def create_plan(plan_name, price, billing_cycle, max_users, features):
        Plan.create(
            plan_name=plan_name,
            price=price,
            billing_cycle=billing_cycle,
            max_users=max_users,
            features=features
        )

        return {
            "status": True,
            "message": "Plan created successfully"
        }