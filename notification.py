from app import mysql


class Notification:

    @staticmethod
    def create(user_id, title, message):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO notifications
            (user_id, title, message)
            VALUES (%s, %s, %s)
            """,
            (user_id, title, message)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_by_user(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT 
                notifications.id,
                notifications.user_id,
                notifications.title,
                notifications.message,
                notifications.is_read,
                notifications.created_at
            FROM notifications
            WHERE notifications.user_id = %s
            ORDER BY notifications.created_at DESC
            """,
            (user_id,)
        )
        notifications = cursor.fetchall()
        cursor.close()
        return notifications

    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT 
                notifications.id,
                users.full_name,
                notifications.title,
                notifications.message,
                notifications.is_read,
                notifications.created_at
            FROM notifications
            JOIN users ON notifications.user_id = users.id
            ORDER BY notifications.created_at DESC
            """
        )
        notifications = cursor.fetchall()
        cursor.close()
        return notifications

    @staticmethod
    def get_by_id(notification_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT 
                notifications.id,
                notifications.user_id,
                users.full_name,
                notifications.title,
                notifications.message,
                notifications.is_read,
                notifications.created_at
            FROM notifications
            JOIN users ON notifications.user_id = users.id
            WHERE notifications.id = %s
            """,
            (notification_id,)
        )
        notification = cursor.fetchone()
        cursor.close()
        return notification

    @staticmethod
    def mark_as_read(notification_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE notifications
            SET is_read = TRUE
            WHERE id = %s
            """,
            (notification_id,)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def mark_all_as_read(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE notifications
            SET is_read = TRUE
            WHERE user_id = %s
            """,
            (user_id,)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete(notification_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            DELETE FROM notifications
            WHERE id = %s
            """,
            (notification_id,)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def total_notifications(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM notifications
            WHERE user_id = %s
            """,
            (user_id,)
        )
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def unread_notifications(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM notifications
            WHERE user_id = %s AND is_read = FALSE
            """,
            (user_id,)
        )
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def read_notifications(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM notifications
            WHERE user_id = %s AND is_read = TRUE
            """,
            (user_id,)
        )
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0