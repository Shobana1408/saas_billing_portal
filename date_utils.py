from datetime import datetime, date, timedelta


def get_current_date():
    return date.today()


def get_current_datetime():
    return datetime.now()


def format_date(value):
    if not value:
        return ""

    if isinstance(value, str):
        return value

    return value.strftime("%Y-%m-%d")


def format_datetime(value):
    if not value:
        return ""

    if isinstance(value, str):
        return value

    return value.strftime("%Y-%m-%d %H:%M:%S")


def add_days(days):
    return date.today() + timedelta(days=days)


def days_between(start_date, end_date):
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()

    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    return (end_date - start_date).days


def is_expired(end_date):
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    return end_date < date.today()