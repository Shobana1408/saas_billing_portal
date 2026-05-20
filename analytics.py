from app import mysql


class Analytics:

    @staticmethod
    def total_revenue():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT SUM(amount_paid)
            FROM payments
            WHERE payment_status = 'success'
            """
        )
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result[0] else 0

    @staticmethod
    def total_users():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        result = cursor.fetchone()
        cursor.close()
        return result[0]

    @staticmethod
    def total_companies():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM companies")
        result = cursor.fetchone()
        cursor.close()
        return result[0]

    @staticmethod
    def active_subscriptions():
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
        return result[0]

    @staticmethod
    def failed_payments():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM payments
            WHERE payment_status = 'failed'
            """
        )
        result = cursor.fetchone()
        cursor.close()
        return result[0]

    @staticmethod
    def monthly_revenue():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT MONTHNAME(payment_date) AS month,
                   SUM(amount_paid) AS revenue
            FROM payments
            WHERE payment_status = 'success'
            GROUP BY MONTH(payment_date), MONTHNAME(payment_date)
            ORDER BY MONTH(payment_date)
            """
        )
        revenue = cursor.fetchall()
        cursor.close()
        return revenue