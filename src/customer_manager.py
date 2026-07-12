from database import Database
from validator import validate_name, validate_mobile
from exceptions import CustomerAlreadyExists


class CustomerManager:

    def __init__(self):
        self.db = Database()

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

    def get_all_customers(self):

        return self.db.fetchall(
            """
            SELECT id, name, mobile
            FROM customers
            ORDER BY name
            """
        )

    def get_customer_by_id(self, customer_id):

        return self.db.fetchone(
            """
            SELECT id, name, mobile
            FROM customers
            WHERE id = ?
            """,
            (customer_id,),
        )

    def find_customer_by_name(self, name):

        return self.db.fetchone(
            """
            SELECT id, name
            FROM customers
            WHERE LOWER(name)=LOWER(?)
            """,
            (name,),
        )