import customtkinter as ctk
from customer_manager import CustomerManager
from transaction_manager import TransactionManager


class LedgerPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.customer_manager = CustomerManager()
        self.transaction_manager = TransactionManager()

        self.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.create_widgets()

    # ---------------------------------------
    # Create Widgets
    # ---------------------------------------

    def create_widgets(self):

        # Heading

        heading = ctk.CTkLabel(
            self,
            text="📒 Customer Ledger",
            font=("Arial", 28, "bold")
        )

        heading.pack(
            pady=(10, 20)
        )

        # Top Frame

        top_frame = ctk.CTkFrame(self)

        top_frame.pack(
            fill="x",
            padx=20
        )

        # Customer

        ctk.CTkLabel(
            top_frame,
            text="Customer"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=15,
            sticky="w"
        )

        self.customer_option = ctk.CTkOptionMenu(
            top_frame,
            values=[]
        )

        self.customer_option.grid(
            row=0,
            column=1,
            padx=10,
            pady=15
        )

        # Show Ledger Button

        self.show_button = ctk.CTkButton(
            top_frame,
            text="📒 Show Ledger"
        )

        self.show_button.grid(
            row=0,
            column=2,
            padx=20,
            pady=15
        )

        # Balance

        self.balance_label = ctk.CTkLabel(
            self,
            text="Current Balance : ₹0.00",
            font=("Arial", 22, "bold")
        )

        self.balance_label.pack(
            pady=20
        )

        # Ledger List

        self.ledger_list = ctk.CTkScrollableFrame(
            self,
            width=850,
            height=350
        )

        self.ledger_list.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            self.ledger_list,
            text="Select a customer and click 'Show Ledger'.",
            font=("Arial", 16)
        ).pack(
            pady=20
        )

        self.load_customers()

    # ---------------------------------------
    # Load Customers
    # ---------------------------------------

    def load_customers(self):

        customers = self.customer_manager.get_all_customers()

        if not customers:

            self.customer_option.configure(
                values=["No Customers"]
            )

            self.customer_option.set(
                "No Customers"
            )

            return

        customer_names = []

        for customer in customers:

            customer_names.append(
                customer[1]
            )

        self.customer_option.configure(
            values=customer_names
        )

        self.customer_option.set(
            customer_names[0]
        )