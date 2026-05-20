from app import mysql


class Subscription:

    @staticmethod
    def create(company_id, plan_id, start_date, end_date, status="active", auto_renew=True):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO subscriptions
            (company_id, plan_id, start_date, end_date, status, auto_renew)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (company_id, plan_id, start_date, end_date, status, auto_renew)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT 
                subscriptions.id,
                companies.company_name,
                plans.plan_name,
                plans.price,
                plans.billing_cycle,
                subscriptions.start_date,
                subscriptions.end_date,
                subscriptions.status,
                subscriptions.auto_renew,
                subscriptions.created_at
            FROM subscriptions
            JOIN companies ON subscriptions.company_id = companies.id
            JOIN plans ON subscriptions.plan_id = plans.id
            ORDER BY subscriptions.created_at DESC
            """
        )
        subscriptions = cursor.fetchall()
        cursor.close()
        return subscriptions

    @staticmethod
    def get_by_id(subscription_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT 
                subscriptions.id,
                subscriptions.company_id,
                companies.company_name,
                subscriptions.plan_id,
                plans.plan_name,
                plans.price,
                plans.billing_cycle,
                plans.max_users,
                subscriptions.start_date,
                subscriptions.end_date,
                subscriptions.status,
                subscriptions.auto_renew,
                subscriptions.created_at
            FROM subscriptions
            JOIN companies ON subscriptions.company_id = companies.id
            JOIN plans ON subscriptions.plan_id = plans.id
            WHERE subscriptions.id = %s
            """,
            (subscription_id,)
        )
        subscription = cursor.fetchone()
        cursor.close()
        return subscription

    @staticmethod
    def update(subscription_id, plan_id, start_date, end_date, status, auto_renew):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE subscriptions
            SET plan_id = %s,
                start_date = %s,
                end_date = %s,
                status = %s,
                auto_renew = %s
            WHERE id = %s
            """,
            (plan_id, start_date, end_date, status, auto_renew, subscription_id)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def upgrade_plan(subscription_id, plan_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE subscriptions
            SET plan_id = %s
            WHERE id = %s
            """,
            (plan_id, subscription_id)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def cancel(subscription_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE subscriptions
            SET status = 'cancelled'
            WHERE id = %s
            """,
            (subscription_id,)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def activate(subscription_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE subscriptions
            SET status = 'active'
            WHERE id = %s
            """,
            (subscription_id,)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def total_active():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM subscriptions
            WHERE status = 'active'
            """
        )
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def total_cancelled():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM subscriptions
            WHERE status = 'cancelled'
            """
        )
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def total_expired():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM subscriptions
            WHERE status = 'expired'
            """
        )
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0