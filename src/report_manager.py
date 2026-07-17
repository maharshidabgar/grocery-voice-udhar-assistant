from database import Database


class ReportManager:

    def __init__(self):
        self.db = Database()

    # ---------------------------------
    # Today's Transactions
    # ---------------------------------

    def get_today_transactions(self):

        return self.db.fetchall(
            """
            SELECT
                customers.name,
                transactions.transaction_type,
                transactions.amount,
                transactions.item_name,
                transactions.note,
                transactions.created_at

            FROM transactions

            INNER JOIN customers
            ON transactions.customer_id = customers.id

            WHERE DATE(transactions.created_at)=DATE('now','localtime')

            ORDER BY transactions.created_at DESC
            """
        )

    # ---------------------------------
    # Today's Summary
    # ---------------------------------

    def get_today_summary(self):

        total_udhar = self.db.fetchone(
            """
            SELECT IFNULL(SUM(amount),0)
            FROM transactions
            WHERE transaction_type='UDHAR'
            AND DATE(created_at)=DATE('now','localtime')
            """
        )[0]

        total_payment = self.db.fetchone(
            """
            SELECT IFNULL(SUM(amount),0)
            FROM transactions
            WHERE transaction_type='PAYMENT'
            AND DATE(created_at)=DATE('now','localtime')
            """
        )[0]

        total_transactions = self.db.fetchone(
            """
            SELECT COUNT(*)
            FROM transactions
            WHERE DATE(created_at)=DATE('now','localtime')
            """
        )[0]

        return (
            total_udhar,
            total_payment,
            total_transactions
        )

    # ---------------------------------
    # Total Outstanding
    # ---------------------------------

    def get_total_outstanding(self):

        rows = self.db.fetchall(
            """
            SELECT
                transaction_type,
                amount
            FROM transactions
            """
        )

        balance = 0

        for transaction_type, amount in rows:

            if transaction_type == "UDHAR":
                balance += amount
            else:
                balance -= amount

        return balance

    # ---------------------------------
    # Total Customers
    # ---------------------------------

    def get_total_customers(self):

        return self.db.fetchone(
            """
            SELECT COUNT(*)
            FROM customers
            """
        )[0]