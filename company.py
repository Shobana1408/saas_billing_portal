from app import mysql


class Company:

    @staticmethod
    def create(company_name, company_email, company_phone, company_address, industry, total_employees):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO companies
            (company_name, company_email, company_phone, company_address, industry, total_employees)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                company_name,
                company_email,
                company_phone,
                company_address,
                industry,
                total_employees
            )
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT 
                id,
                company_name,
                company_email,
                company_phone,
                company_address,
                industry,
                total_employees,
                created_at
            FROM companies
            ORDER BY created_at DESC
            """
        )
        companies = cursor.fetchall()
        cursor.close()
        return companies

    @staticmethod
    def get_by_id(company_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT 
                id,
                company_name,
                company_email,
                company_phone,
                company_address,
                industry,
                total_employees,
                created_at
            FROM companies
            WHERE id = %s
            """,
            (company_id,)
        )
        company = cursor.fetchone()
        cursor.close()
        return company

    @staticmethod
    def update(company_id, company_name, company_email, company_phone, company_address, industry, total_employees):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE companies
            SET company_name = %s,
                company_email = %s,
                company_phone = %s,
                company_address = %s,
                industry = %s,
                total_employees = %s
            WHERE id = %s
            """,
            (
                company_name,
                company_email,
                company_phone,
                company_address,
                industry,
                total_employees,
                company_id
            )
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete(company_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM companies WHERE id = %s", (company_id,))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def count_users(company_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM users
            WHERE company_id = %s
            """,
            (company_id,)
        )
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def count_subscriptions(company_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM subscriptions
            WHERE company_id = %s
            """,
            (company_id,)
        )
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def get_company_summary(company_id):
        cursor = mysql.connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM users
            WHERE company_id = %s
            """,
            (company_id,)
        )
        total_users = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM subscriptions
            WHERE company_id = %s
            """,
            (company_id,)
        )
        total_subscriptions = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM invoices
            WHERE company_id = %s
            """,
            (company_id,)
        )
        total_invoices = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COALESCE(SUM(total_amount), 0)
            FROM invoices
            WHERE company_id = %s
            """,
            (company_id,)
        )
        total_billing = cursor.fetchone()[0]

        cursor.close()

        return {
            "total_users": total_users,
            "total_subscriptions": total_subscriptions,
            "total_invoices": total_invoices,
            "total_billing": total_billing
        }