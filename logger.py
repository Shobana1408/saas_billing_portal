import logging
import os
from datetime import datetime


LOG_FOLDER = "logs"

if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)


log_file = os.path.join(LOG_FOLDER, "app.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_info(message):
    logging.info(message)


def log_warning(message):
    logging.warning(message)


def log_error(message):
    logging.error(message)


def log_activity(user_id, action):
    message = f"User ID {user_id}: {action}"
    logging.info(message)


def create_log_message(action):
    return f"{datetime.now()} - {action}"