from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user

from models.user import User


class AuthService:

    @staticmethod
    def register_user(full_name, email, password, role_id, company_id):
        existing_user = User.get_by_email(email)

        if existing_user:
            return {
                "status": False,
                "message": "Email already registered"
            }

        hashed_password = generate_password_hash(password)

        User.create(
            full_name=full_name,
            email=email,
            password=hashed_password,
            role_id=role_id,
            company_id=company_id
        )

        return {
            "status": True,
            "message": "User registered successfully"
        }

    @staticmethod
    def login_user_account(email, password):
        user = User.get_by_email(email)

        if not user:
            return {
                "status": False,
                "message": "Invalid email or password",
                "user": None
            }

        if not check_password_hash(user.password, password):
            return {
                "status": False,
                "message": "Invalid email or password",
                "user": None
            }

        if user.status == "blocked":
            return {
                "status": False,
                "message": "Your account is blocked",
                "user": None
            }

        login_user(user)

        return {
            "status": True,
            "message": "Login successful",
            "user": user
        }

    @staticmethod
    def logout_user_account():
        logout_user()
        return {
            "status": True,
            "message": "Logged out successfully"
        }

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    @staticmethod
    def verify_password(hashed_password, password):
        return check_password_hash(hashed_password, password)