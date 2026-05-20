from models.notification import Notification


class NotificationService:

    @staticmethod
    def create_notification(user_id, title, message):
        Notification.create(
            user_id=user_id,
            title=title,
            message=message
        )

        return {
            "status": True,
            "message": "Notification created successfully"
        }

    @staticmethod
    def get_user_notifications(user_id):
        return Notification.get_by_user(user_id)

    @staticmethod
    def mark_notification_as_read(notification_id):
        Notification.mark_as_read(notification_id)

        return {
            "status": True,
            "message": "Notification marked as read"
        }

    @staticmethod
    def delete_notification(notification_id):
        Notification.delete(notification_id)

        return {
            "status": True,
            "message": "Notification deleted successfully"
        }

    @staticmethod
    def send_payment_reminder(user_id, invoice_number):
        title = "Payment Reminder"
        message = f"Your invoice {invoice_number} is pending. Please complete the payment."

        Notification.create(user_id, title, message)

        return {
            "status": True,
            "message": "Payment reminder sent"
        }