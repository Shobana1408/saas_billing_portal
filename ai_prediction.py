from app import mysql


class AIPrediction:

    @staticmethod
    def create(prediction_type, prediction_result):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO ai_predictions
            (prediction_type, prediction_result)
            VALUES (%s, %s)
            """,
            (prediction_type, prediction_result)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT *
            FROM ai_predictions
            ORDER BY generated_at DESC
            """
        )
        predictions = cursor.fetchall()
        cursor.close()
        return predictions

    @staticmethod
    def get_by_type(prediction_type):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT *
            FROM ai_predictions
            WHERE prediction_type = %s
            ORDER BY generated_at DESC
            """,
            (prediction_type,)
        )
        predictions = cursor.fetchall()
        cursor.close()
        return predictions