from werkzeug.security import generate_password_hash
from models.user import User


class UserService:

    @staticmethod
    def create_user(full_name, email, password, role_id, company_id, status="active"):
        hashed_password = generate_password_hash(password)

        User.create(
            full_name=full_name,
            email=email,
            password=hashed_password,
            role_id=role_id,
            company_id=company_id,
            status=status
        )

        return {
            "status": True,
            "message": "User created successfully"
        }

    @staticmethod
    def get_all_users():
        return User.get_all()

    @staticmethod
    def get_user_details(user_id):
        return User.get_by_id(user_id)

    @staticmethod
    def get_user_by_email(email):
        return User.get_by_email(email)

    @staticmethod
    def update_user_status(user_id, status):
        User.update_status(user_id, status)

        return {
            "status": True,
            "message": "User status updated successfully"
        }

    @staticmethod
    def is_active_user(user):
        return user.status == "active"