from app import mysql


class Payment:

    @staticmethod
    def create(invoice_id, payment_method, payment_status, transaction_id, amount_paid):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO payments
            (invoice_id, payment_method, payment_status, transaction_id, amount_paid)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                invoice_id,
                payment_method,
                payment_status,
                transaction_id,
                amount_paid
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
                payments.id,
                invoices.invoice_number,
                companies.company_name,
                payments.payment_method,
                payments.payment_status,
                payments.transaction_id,
                payments.amount_paid,
                payments.payment_date
            FROM payments
            JOIN invoices ON payments.invoice_id = invoices.id
            JOIN companies ON invoices.company_id = companies.id
            ORDER BY payments.payment_date DESC
            """
        )
        payments = cursor.fetchall()
        cursor.close()
        return payments

    @staticmethod
    def get_by_id(payment_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT 
                payments.id,
                invoices.invoice_number,
                companies.company_name,
                payments.payment_method,
                payments.payment_status,
                payments.transaction_id,
                payments.amount_paid,
                payments.payment_date
            FROM payments
            JOIN invoices ON payments.invoice_id = invoices.id
            JOIN companies ON invoices.company_id = companies.id
            WHERE payments.id = %s
            """,
            (payment_id,)
        )
        payment = cursor.fetchone()
        cursor.close()
        return payment

    @staticmethod
    def get_by_invoice(invoice_id):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT *
            FROM payments
            WHERE invoice_id = %s
            ORDER BY payment_date DESC
            """,
            (invoice_id,)
        )
        payments = cursor.fetchall()
        cursor.close()
        return payments

    @staticmethod
    def total_payments():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM payments")
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def successful_payments():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM payments WHERE payment_status = 'success'")
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def failed_payments():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM payments WHERE payment_status = 'failed'")
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def pending_payments():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM payments WHERE payment_status = 'pending'")
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    @staticmethod
    def total_success_amount():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT COALESCE(SUM(amount_paid), 0)
            FROM payments
            WHERE payment_status = 'success'
            """
        )
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0