from database import Database

class TransactionManager:

    def __init__(self):
        self.db = Database()

    # ---------------------------------
    # Add Udhar
    # ---------------------------------

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

    # ---------------------------------
    # Add Payment
    # ---------------------------------

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

    # ---------------------------------
    # Customer Transactions
    # ---------------------------------

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
            WHERE customer_id = ?
            ORDER BY created_at
            """,
            (customer_id,),
        )

    # ---------------------------------
    # Customer Balance
    # ---------------------------------

    def get_balance(self, customer_id):

        rows = self.db.fetchall(
            """
            SELECT
                transaction_type,
                amount
            FROM transactions
            WHERE customer_id = ?
            """,
            (customer_id,),
        )

        balance = 0.0

        for transaction_type, amount in rows:

            if transaction_type == "UDHAR":
                balance += amount

            elif transaction_type == "PAYMENT":
                balance -= amount

        return balance

    # ---------------------------------
    # Total Udhar
    # ---------------------------------

    def get_total_udhar(self, customer_id):

        result = self.db.fetchone(
            """
            SELECT COALESCE(SUM(amount),0)
            FROM transactions
            WHERE customer_id=?
            AND transaction_type='UDHAR'
            """,
            (customer_id,)
        )

        return result[0]


    # ---------------------------------
    # Total Payment
    # ---------------------------------

    def get_total_payment(self, customer_id):

        result = self.db.fetchone(
            """
            SELECT COALESCE(SUM(amount),0)
            FROM transactions
            WHERE customer_id=?
            AND transaction_type='PAYMENT'
            """,
            (customer_id,)
        )

        return result[0]
    # ---------------------------------
    # Customer Ledger
    # ---------------------------------

    def get_customer_ledger(self, customer_id):

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
            WHERE customer_id = ?
            ORDER BY created_at
            """,
            (customer_id,),
        )

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
    # Delete Transaction
    # ---------------------------------

    def delete_transaction(self, transaction_id):

        self.db.execute(
            """
            DELETE FROM transactions
            WHERE id = ?
            """,
            (transaction_id,),
        )

        return "Transaction deleted successfully."

    # ---------------------------------
    # Today's Udhar
    # ---------------------------------

    def get_today_udhar(self):

        result = self.db.fetchone(
            """
            SELECT COALESCE(SUM(amount),0)
            FROM transactions
            WHERE transaction_type='UDHAR'
            AND DATE(created_at)=DATE('now','localtime')
            """
        )

        return result[0]


    # ---------------------------------
    # Today's Payment
    # ---------------------------------

    def get_today_payment(self):

        result = self.db.fetchone(
            """
            SELECT COALESCE(SUM(amount),0)
            FROM transactions
            WHERE transaction_type='PAYMENT'
            AND DATE(created_at)=DATE('now','localtime')
            """
        )

        return result[0]


    # ---------------------------------
    # Today's Transaction Count
    # ---------------------------------

    def get_today_transaction_count(self):

        result = self.db.fetchone(
            """
            SELECT COUNT(*)
            FROM transactions
            WHERE DATE(created_at)=DATE('now','localtime')
            """
        )

        return result[0]


    # ---------------------------------
    # Total Transaction Count
    # ---------------------------------

    def get_total_transaction_count(self):

        result = self.db.fetchone(
            """
            SELECT COUNT(*)
            FROM transactions
            """
        )

        return result[0]


    # ---------------------------------
    # Total Collection
    # ---------------------------------

    def get_total_collection(self):

        result = self.db.fetchone(
            """
            SELECT COALESCE(SUM(amount),0)
            FROM transactions
            WHERE transaction_type='PAYMENT'
            """
        )

        return result[0]