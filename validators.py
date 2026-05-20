import re


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_password(password):
    if len(password) < 6:
        return False, "Password must be at least 6 characters long"

    return True, "Valid password"


def validate_phone(phone):
    pattern = r"^[0-9]{10}$"
    return re.match(pattern, phone) is not None


def validate_required(value):
    return value is not None and str(value).strip() != ""


def validate_positive_number(value):
    try:
        return float(value) >= 0
    except:
        return False


def validate_date_range(start_date, end_date):
    if not start_date or not end_date:
        return False

    return start_date <= end_date