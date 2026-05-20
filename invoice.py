from app import mysql


class Invoice:

    @staticmethod
    def create(company_id, subscription_id, invoice_number, amount, tax, total_amount, due_date, status="unpaid"):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO invoices
            (company_id, subscription_id, invoice_number, amount, tax, total_amount, due_date, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                company_id,
                subscription_id,
                invoice_number,
                amount,
                tax,
                total_amount,
                due_date,
                status
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
                invoices.id,
                invoices.invoice_number,
                companies.company_name,
                invoices.amount,
                invoices.tax,
                invoices.total_amount,
                invoices.due_date,
                invoices.status,
                invoices.created_at
            FROM invoices
            JOIN companies ON invoices.company_id = companies.id
            ORDER BY invoices.created_at DESC
            """
        )
        invoices = cursor.fetchall()
        cursor.close()
        return invoices

    @staticmethod
    def get_by_id(invoice_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT 
                invoices.id,
                invoices.company_id,
                companies.company_name,
                invoices.subscription_id,
                invoices.invoice_number,
                invoices.amount,
                invoices.tax,
                invoices.total_amount,
                invoices.due_date,
                invoices.status,
                invoices.created_at
            FROM invoices
            JOIN companies ON invoices.company_id = companies.id
            WHERE invoices.id = %s
            """,
            (invoice_id,)
        )
        invoice = cursor.fetchone()
        cursor.close()
        return invoice

    @staticmethod
    def update_status(invoice_id, status):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE invoices
            SET status = %s
            WHERE id = %s
            """,
            (status, invoice_id)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete(invoice_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM invoices WHERE id = %s", (invoice_id,))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def total_invoices():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM invoices")
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def paid_invoices():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM invoices WHERE status = 'paid'")
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def unpaid_invoices():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM invoices WHERE status = 'unpaid'")
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def overdue_invoices():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM invoices WHERE status = 'overdue'")
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def total_invoice_value():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COALESCE(SUM(total_amount), 0) FROM invoices")
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0