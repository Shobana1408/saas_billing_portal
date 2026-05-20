from app import mysql


class Plan:

    @staticmethod
    def create(plan_name, price, billing_cycle, max_users, features):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO plans
            (plan_name, price, billing_cycle, max_users, features)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (plan_name, price, billing_cycle, max_users, features)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT 
                id,
                plan_name,
                price,
                billing_cycle,
                max_users,
                features,
                created_at
            FROM plans
            ORDER BY price ASC
            """
        )
        plans = cursor.fetchall()
        cursor.close()
        return plans

    @staticmethod
    def get_by_id(plan_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT 
                id,
                plan_name,
                price,
                billing_cycle,
                max_users,
                features,
                created_at
            FROM plans
            WHERE id = %s
            """,
            (plan_id,)
        )
        plan = cursor.fetchone()
        cursor.close()
        return plan

    @staticmethod
    def update(plan_id, plan_name, price, billing_cycle, max_users, features):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE plans
            SET plan_name = %s,
                price = %s,
                billing_cycle = %s,
                max_users = %s,
                features = %s
            WHERE id = %s
            """,
            (plan_name, price, billing_cycle, max_users, features, plan_id)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete(plan_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM plans WHERE id = %s", (plan_id,))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def count_subscriptions(plan_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM subscriptions
            WHERE plan_id = %s
            """,
            (plan_id,)
        )
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0