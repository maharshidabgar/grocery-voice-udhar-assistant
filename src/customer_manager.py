from src.database import Database
from src.validator import validate_name, validate_mobile
from src.exceptions import CustomerAlreadyExists


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
    # Find Customer By Voice Name
    # ---------------------------------------

    def find_customer_by_voice_name(self, voice_name):

        if not voice_name:

            return None

        voice_name = voice_name.lower().strip()

        # Common Gujarati suffixes
        remove_words = [
            "bhai",
            "ben",
            "kaka",
            "kaki",
            "dada",
            "dadi",
            "mama",
            "mami",
            "sir",
            "ji",
        ]

        words = voice_name.split()

        filtered = []

        for word in words:

            if word not in remove_words:

                filtered.append(word)

        clean_name = " ".join(filtered)

        customers = self.get_all_customers()

        # Exact Match
        for customer in customers:

            if customer[1].lower() == clean_name:

                return customer

        # Startswith Match
        for customer in customers:

            if customer[1].lower().startswith(clean_name):

                return customer

        # Contains Match
        for customer in customers:

            if clean_name in customer[1].lower():

                return customer

        return None

    # ---------------------------------------
    # Suggest Similar Customers
    # ---------------------------------------

    def suggest_customers(self, voice_name):

        if not voice_name:

            return []

        voice_name = voice_name.lower().strip()

        suggestions = []

        customers = self.get_all_customers()

        for customer in customers:

            name = customer[1].lower()

            if (
                voice_name in name
                or name.startswith(voice_name)
                or voice_name.startswith(name)
            ):

                suggestions.append(customer)

        return suggestions
    
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