from database import Database


class TransactionManager:

    def __init__(self):
        self.db = Database()

    def add_udhar(self, customer_id, amount, item_name="", note=""):

        self.db.execute(
            """
            INSERT INTO transactions
            (
                customer_id,
                transaction_type,
                amount,
                item_name,
                note
            )
            VALUES
            (?, 'UDHAR', ?, ?, ?)
            """,
            (
                customer_id,
                amount,
                item_name,
                note,
            ),
        )

        return "Udhar added successfully."

    def add_payment(self, customer_id, amount, note=""):

        self.db.execute(
            """
            INSERT INTO transactions
            (
                customer_id,
                transaction_type,
                amount,
                note
            )
            VALUES
            (?, 'PAYMENT', ?, ?)
            """,
            (
                customer_id,
                amount,
                note,
            ),
        )

        return "Payment added successfully."

    def get_customer_transactions(self, customer_id):

        return self.db.fetchall(
            """
            SELECT
                id,
                transaction_type,
                amount,
                item_name,
                note,
                created_at
            FROM transactions
            WHERE customer_id=?
            ORDER BY created_at
            """,
            (
                customer_id,
            ),
        )

    def get_balance(self, customer_id):

        rows = self.db.fetchall(
            """
            SELECT
                transaction_type,
                amount
            FROM transactions
            WHERE customer_id=?
            """,
            (
                customer_id,
            ),
        )

        balance = 0

        for transaction_type, amount in rows:

            if transaction_type == "UDHAR":
                balance += amount

            else:
                balance -= amount

        return balance

    def delete_transaction(self, transaction_id):

        self.db.execute(
            """
            DELETE FROM transactions
            WHERE id=?
            """,
            (
                transaction_id,
            ),
        )

        return "Transaction deleted successfully."