import customtkinter as ctk

from transaction_manager import TransactionManager
from customer_manager import CustomerManager


class ReportsPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.transaction_manager = TransactionManager()
        self.customer_manager = CustomerManager()

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
            text="📊 Reports Dashboard",
            font=("Arial", 30, "bold")
        )

        heading.pack(
            pady=(10, 30)
        )

        cards = ctk.CTkFrame(self)

        cards.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        cards.grid_columnconfigure((0, 1), weight=1)

        self.udhar_card = self.create_card(
            cards,
            "🟢 Today's Udhar",
            "₹0"
        )

        self.udhar_card.grid(
            row=0,
            column=0,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        self.payment_card = self.create_card(
            cards,
            "🔵 Today's Payment",
            "₹0"
        )

        self.payment_card.grid(
            row=0,
            column=1,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        self.transaction_card = self.create_card(
            cards,
            "📄 Today's Transactions",
            "0"
        )

        self.transaction_card.grid(
            row=1,
            column=0,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        self.collection_card = self.create_card(
            cards,
            "💰 Total Collection",
            "₹0"
        )

        self.collection_card.grid(
            row=1,
            column=1,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        self.load_reports()

    # ---------------------------------------
    # Card
    # ---------------------------------------

    def create_card(self, parent, title, value):

        card = ctk.CTkFrame(parent)

        ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 18, "bold")
        ).pack(
            pady=(20, 10)
        )

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 28, "bold")
        )

        value_label.pack(
            pady=(0, 20)
        )

        card.value_label = value_label

        return card

    # ---------------------------------------
    # Load Reports
    # ---------------------------------------

    def load_reports(self):

        self.udhar_card.value_label.configure(
            text=f"₹{self.transaction_manager.get_today_udhar():.2f}"
        )

        self.payment_card.value_label.configure(
            text=f"₹{self.transaction_manager.get_today_payment():.2f}"
        )

        self.transaction_card.value_label.configure(
            text=str(
                self.transaction_manager.get_today_transaction_count()
            )
        )

        self.collection_card.value_label.configure(
            text=f"₹{self.transaction_manager.get_total_collection():.2f}"
        )