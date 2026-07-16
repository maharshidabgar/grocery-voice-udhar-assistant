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

        heading = ctk.CTkLabel(
            self,
            text="📒 Customer Ledger",
            font=("Arial", 28, "bold")
        )

        heading.pack(
            pady=(10, 20)
        )

        # Customer Selection Frame

        top_frame = ctk.CTkFrame(self)

        top_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        top_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            top_frame,
            text="Customer"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.customer_option = ctk.CTkOptionMenu(
            top_frame,
            values=["Loading..."],
            width=220,
            command=self.customer_changed
        )

        self.customer_option.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="w"
        )

        # ---------------------------------------
        # Summary Cards
        # ---------------------------------------

        summary_frame = ctk.CTkFrame(top_frame)

        summary_frame.grid(
            row=0,
            column=2,
            padx=20,
            pady=10,
            sticky="e"
        )

        self.udhar_label = ctk.CTkLabel(
            summary_frame,
            text="🟢 Udhar : ₹0",
            font=("Arial", 15, "bold")
        )

        self.udhar_label.pack(
            anchor="w",
            padx=10,
            pady=2
        )

        self.payment_label = ctk.CTkLabel(
            summary_frame,
            text="🔵 Payment : ₹0",
            font=("Arial", 15, "bold")
        )

        self.payment_label.pack(
            anchor="w",
            padx=10,
            pady=2
        )

        self.balance_label = ctk.CTkLabel(
            summary_frame,
            text="🔴 Balance : ₹0",
            font=("Arial", 16, "bold")
        )

        self.balance_label.pack(
            anchor="w",
            padx=10,
            pady=2
        )

        self.ledger_frame = ctk.CTkScrollableFrame(
            self,
            width=900,
            height=450
        )

        self.ledger_frame.pack(
            fill="both",
            expand=True,
            padx=20,
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

            customer_names.append(customer[1])

        self.customer_option.configure(
            values=customer_names
        )

        self.customer_option.set(
            customer_names[0]
        )

        self.customer_changed(
            customer_names[0]
        )

    # ---------------------------------------
    # Customer Changed
    # ---------------------------------------

    def customer_changed(self, selected_name):

        # Clear old ledger
        for widget in self.ledger_frame.winfo_children():
            widget.destroy()

        # Get Customer
        customer = self.customer_manager.find_customer_by_name(
            selected_name
        )

        if not customer:
            return

        customer_id = customer[0]

        # ---------------------------------------
        # Summary
        # ---------------------------------------

        total_udhar = self.transaction_manager.get_total_udhar(
            customer_id
        )

        total_payment = self.transaction_manager.get_total_payment(
            customer_id
        )

        balance = self.transaction_manager.get_balance(
            customer_id
        )

        self.udhar_label.configure(
            text=f"🟢 Udhar : ₹{total_udhar:.2f}"
        )

        self.payment_label.configure(
            text=f"🔵 Payment : ₹{total_payment:.2f}"
        )

        self.balance_label.configure(
            text=f"🔴 Balance : ₹{balance:.2f}"
        )

        # Ledger Data
        transactions = self.transaction_manager.get_customer_ledger(
            customer_id
        )

        if not transactions:

            ctk.CTkLabel(
                self.ledger_frame,
                text="No Transactions Found",
                font=("Arial", 18)
            ).pack(
                pady=20
            )

            return

        # Header
        header = ctk.CTkFrame(
            self.ledger_frame
        )

        header.pack(
            fill="x",
            pady=5
        )

        headings = [
            "ID",
            "Type",
            "Amount",
            "Item",
            "Note",
            "Date"
        ]

        for col, title in enumerate(headings):

            ctk.CTkLabel(
                header,
                text=title,
                width=120,
                font=("Arial", 14, "bold")
            ).grid(
                row=0,
                column=col,
                padx=5
            )

        # Rows
        for transaction in transactions:

            row = ctk.CTkFrame(
                self.ledger_frame
            )

            row.pack(
                fill="x",
                pady=2
            )

            for col, value in enumerate(transaction):

                ctk.CTkLabel(
                    row,
                    text=str(value),
                    width=120,
                    anchor="w"
                ).grid(
                    row=0,
                    column=col,
                    padx=5
                )