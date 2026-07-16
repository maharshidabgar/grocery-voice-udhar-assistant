from src.database import Database


class DashboardManager:

    def __init__(self):
        self.db = Database()

    # -----------------------------
    # Total Customers
    # -----------------------------
    def total_customers(self):

        row = self.db.fetchone(
            """
            SELECT COUNT(*)
            FROM customers
            """
        )

        return row[0]

    # -----------------------------
    # Today's Udhar
    # -----------------------------
    def today_udhar(self):

        row = self.db.fetchone(
            """
            SELECT
                IFNULL(SUM(amount),0)
            FROM transactions
            WHERE
                transaction_type='UDHAR'
                AND DATE(created_at)=DATE('now','localtime')
            """
        )

        return row[0]

    # -----------------------------
    # Today's Payment
    # -----------------------------
    def today_payment(self):

        row = self.db.fetchone(
            """
            SELECT
                IFNULL(SUM(amount),0)
            FROM transactions
            WHERE
                transaction_type='PAYMENT'
                AND DATE(created_at)=DATE('now','localtime')
            """
        )

        return row[0]

    # -----------------------------
    # Pending Balance
    # -----------------------------
    def pending_balance(self):

        udhar = self.db.fetchone(
            """
            SELECT IFNULL(SUM(amount),0)
            FROM transactions
            WHERE transaction_type='UDHAR'
            """
        )[0]

        payment = self.db.fetchone(
            """
            SELECT IFNULL(SUM(amount),0)
            FROM transactions
            WHERE transaction_type='PAYMENT'
            """
        )[0]

        return udhar - payment