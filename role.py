from app import mysql


class Role:

    @staticmethod
    def create(role_name, description):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO roles (role_name, description)
            VALUES (%s, %s)
            """,
            (role_name, description)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM roles")
        roles = cursor.fetchall()
        cursor.close()
        return roles

    @staticmethod
    def get_by_id(role_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM roles WHERE id = %s", (role_id,))
        role = cursor.fetchone()
        cursor.close()
        return role

    @staticmethod
    def get_role_name(role_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT role_name FROM roles WHERE id = %s", (role_id,))
        role = cursor.fetchone()
        cursor.close()

        if role:
            return role[0]
        return None