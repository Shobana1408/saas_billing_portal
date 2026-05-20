from werkzeug.security import generate_password_hash, check_password_hash
import secrets


def hash_password(password):
    return generate_password_hash(password)


def verify_password(hashed_password, password):
    return check_password_hash(hashed_password, password)


def generate_token(length=32):
    return secrets.token_hex(length)


def generate_otp(length=6):
    otp = ""

    for _ in range(length):
        otp += str(secrets.randbelow(10))

    return otp


def generate_secret_key():
    return secrets.token_hex(32)