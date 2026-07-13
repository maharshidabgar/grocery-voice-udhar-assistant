from database import Database
from validator import validate_name, validate_mobile
from exceptions import CustomerAlreadyExists


class CustomerManager:

    def __init__(self):
        self.db = Database()

    # ---------------------------------------
    # Add Customer
    # ---------------------------------------

    def add_customer(self, name, mobile=""):

        name = validate_name(name)
        mobile = validate_mobile(mobile)

        existing = self.db.fetchone(
            """
            SELECT id
            FROM customers
            WHERE LOWER(name)=LOWER(?)
            """,
            (name,),
        )

        if existing:
            raise CustomerAlreadyExists(
                f"{name} already exists."
            )

        self.db.execute(
            """
            INSERT INTO customers(name,mobile)
            VALUES(?,?)
            """,
            (name, mobile),
        )

        return f"{name} added successfully."

    # ---------------------------------------
    # Get All Customers
    # ---------------------------------------

    def get_all_customers(self):

        return self.db.fetchall(
            """
            SELECT id, name, mobile
            FROM customers
            ORDER BY name
            """
        )

    # ---------------------------------------
    # Get Customer By ID
    # ---------------------------------------

    def get_customer_by_id(self, customer_id):

        return self.db.fetchone(
            """
            SELECT id, name, mobile
            FROM customers
            WHERE id = ?
            """,
            (customer_id,),
        )

    # ---------------------------------------
    # Find Customer By Name
    # ---------------------------------------

    def find_customer_by_name(self, name):

        return self.db.fetchone(
            """
            SELECT id, name
            FROM customers
            WHERE LOWER(name)=LOWER(?)
            """,
            (name,),
        )

    # ---------------------------------------
    # Update Customer
    # ---------------------------------------

    def update_customer(self, customer_id, name, mobile):

        name = validate_name(name)
        mobile = validate_mobile(mobile)

        self.db.execute(
            """
            UPDATE customers
            SET
                name = ?,
                mobile = ?
            WHERE id = ?
            """,
            (
                name,
                mobile,
                customer_id,
            ),
        )

        return "Customer updated successfully."

    # ---------------------------------------
    # Delete Customer
    # ---------------------------------------

    def delete_customer(self, customer_id):

        self.db.execute(
            """
            DELETE FROM customers
            WHERE id = ?
            """,
            (customer_id,),
        )

        return "Customer deleted successfully."