from app import mysql


class AuditLog:

    @staticmethod
    def create(user_id, action, ip_address):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO audit_logs
            (user_id, action, ip_address)
            VALUES (%s, %s, %s)
            """,
            (user_id, action, ip_address)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT audit_logs.id,
                   users.full_name,
                   audit_logs.action,
                   audit_logs.ip_address,
                   audit_logs.created_at
            FROM audit_logs
            JOIN users ON audit_logs.user_id = users.id
            ORDER BY audit_logs.created_at DESC
            """
        )
        logs = cursor.fetchall()
        cursor.close()
        return logs

    @staticmethod
    def get_by_user(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT * FROM audit_logs
            WHERE user_id = %s
            ORDER BY created_at DESC
            """,
            (user_id,)
        )
        logs = cursor.fetchall()
        cursor.close()
        return logs