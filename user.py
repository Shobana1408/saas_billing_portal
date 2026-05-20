from flask_login import UserMixin
from app import mysql


class User(UserMixin):
    def __init__(
        self,
        id,
        full_name,
        email,
        password,
        role_id,
        company_id=None,
        profile_image=None,
        status="active"
    ):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.password = password
        self.role_id = role_id
        self.company_id = company_id
        self.profile_image = profile_image
        self.status = status

    @staticmethod
    def get_by_id(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT id, full_name, email, password, role_id, company_id, profile_image, status
            FROM users
            WHERE id = %s
            """,
            (user_id,)
        )
        user = cursor.fetchone()
        cursor.close()

        if user:
            return User(
                id=user[0],
                full_name=user[1],
                email=user[2],
                password=user[3],
                role_id=user[4],
                company_id=user[5],
                profile_image=user[6],
                status=user[7]
            )

        return None

    @staticmethod
    def get_by_email(email):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT id, full_name, email, password, role_id, company_id, profile_image, status
            FROM users
            WHERE email = %s
            """,
            (email,)
        )
        user = cursor.fetchone()
        cursor.close()

        if user:
            return User(
                id=user[0],
                full_name=user[1],
                email=user[2],
                password=user[3],
                role_id=user[4],
                company_id=user[5],
                profile_image=user[6],
                status=user[7]
            )

        return None

    @staticmethod
    def create(full_name, email, password, role_id, company_id, status="active"):
        if company_id == "":
            company_id = None

        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO users 
            (full_name, email, password, role_id, company_id, status)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (full_name, email, password, role_id, company_id, status)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT 
                users.id,
                users.full_name,
                users.email,
                roles.role_name,
                COALESCE(companies.company_name, 'No Company') AS company_name,
                users.status,
                users.created_at
            FROM users
            JOIN roles ON users.role_id = roles.id
            LEFT JOIN companies ON users.company_id = companies.id
            ORDER BY users.created_at DESC
            """
        )
        users = cursor.fetchall()
        cursor.close()
        return users

    @staticmethod
    def get_details_by_id(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT 
                users.id,
                users.full_name,
                users.email,
                users.role_id,
                roles.role_name,
                users.company_id,
                COALESCE(companies.company_name, 'No Company') AS company_name,
                users.status,
                users.created_at
            FROM users
            JOIN roles ON users.role_id = roles.id
            LEFT JOIN companies ON users.company_id = companies.id
            WHERE users.id = %s
            """,
            (user_id,)
        )
        user = cursor.fetchone()
        cursor.close()
        return user

    @staticmethod
    def update_status(user_id, status):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE users 
            SET status = %s 
            WHERE id = %s
            """,
            (status, user_id)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_profile(user_id, full_name, email):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE users
            SET full_name = %s,
                email = %s
            WHERE id = %s
            """,
            (full_name, email, user_id)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_role(user_id, role_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE users
            SET role_id = %s
            WHERE id = %s
            """,
            (role_id, user_id)
        )
        mysql.connection.commit()
        cursor.close()