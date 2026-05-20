from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from models.notification import Notification

notification_bp = Blueprint("notifications", __name__)


@notification_bp.route("/notifications")
@login_required
def notification_list():
    notifications = Notification.get_by_user(current_user.id)

    summary = {
        "total": Notification.total_notifications(current_user.id),
        "unread": Notification.unread_notifications(current_user.id),
        "read": Notification.read_notifications(current_user.id)
    }

    return render_template(
        "notifications/notification_list.html",
        notifications=notifications,
        summary=summary
    )


@notification_bp.route("/notification/<int:notification_id>")
@login_required
def notification_details(notification_id):
    notification = Notification.get_by_id(notification_id)

    if not notification:
        flash("Notification not found.", "danger")
        return redirect(url_for("notifications.notification_list"))

    if int(notification[1]) != int(current_user.id) and int(current_user.role_id) != 1:
        flash("You do not have permission to view this notification.", "danger")
        return redirect(url_for("notifications.notification_list"))

    Notification.mark_as_read(notification_id)

    notification = Notification.get_by_id(notification_id)

    return render_template(
        "notifications/notification_details.html",
        notification=notification
    )


@notification_bp.route("/notification/read/<int:notification_id>")
@login_required
def mark_notification_read(notification_id):
    notification = Notification.get_by_id(notification_id)

    if not notification:
        flash("Notification not found.", "danger")
        return redirect(url_for("notifications.notification_list"))

    if int(notification[1]) != int(current_user.id) and int(current_user.role_id) != 1:
        flash("You do not have permission to update this notification.", "danger")
        return redirect(url_for("notifications.notification_list"))

    Notification.mark_as_read(notification_id)

    flash("Notification marked as read.", "success")
    return redirect(url_for("notifications.notification_list"))


@notification_bp.route("/notifications/mark-all-read")
@login_required
def mark_all_notifications_read():
    Notification.mark_all_as_read(current_user.id)

    flash("All notifications marked as read.", "success")
    return redirect(url_for("notifications.notification_list"))


@notification_bp.route("/notification/delete/<int:notification_id>")
@login_required
def delete_notification(notification_id):
    notification = Notification.get_by_id(notification_id)

    if not notification:
        flash("Notification not found.", "danger")
        return redirect(url_for("notifications.notification_list"))

    if int(notification[1]) != int(current_user.id) and int(current_user.role_id) != 1:
        flash("You do not have permission to delete this notification.", "danger")
        return redirect(url_for("notifications.notification_list"))

    Notification.delete(notification_id)

    flash("Notification deleted successfully.", "success")
    return redirect(url_for("notifications.notification_list"))