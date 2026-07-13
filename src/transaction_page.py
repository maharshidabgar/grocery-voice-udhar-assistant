import customtkinter as ctk


class TransactionPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

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
            text="💰 Transaction Management",
            font=("Arial", 28, "bold")
        )

        heading.pack(pady=(10, 20))

        # Form

        form = ctk.CTkFrame(self)

        form.pack(
            fill="x",
            padx=20
        )

        # Customer

        ctk.CTkLabel(
            form,
            text="Customer"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.customer_option = ctk.CTkOptionMenu(
            form,
            values=["Select Customer"]
        )

        self.customer_option.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        # Transaction Type

        ctk.CTkLabel(
            form,
            text="Transaction Type"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.transaction_type = ctk.StringVar(
            value="UDHAR"
        )

        udhar_radio = ctk.CTkRadioButton(
            form,
            text="Udhar",
            variable=self.transaction_type,
            value="UDHAR"
        )

        udhar_radio.grid(
            row=1,
            column=1,
            sticky="w",
            padx=10
        )

        payment_radio = ctk.CTkRadioButton(
            form,
            text="Payment",
            variable=self.transaction_type,
            value="PAYMENT"
        )

        payment_radio.grid(
            row=1,
            column=2,
            sticky="w",
            padx=10
        )

        # Amount

        ctk.CTkLabel(
            form,
            text="Amount"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.amount_entry = ctk.CTkEntry(
            form,
            width=250
        )

        self.amount_entry.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        # Item Name

        ctk.CTkLabel(
            form,
            text="Item Name"
        ).grid(
            row=3,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.item_entry = ctk.CTkEntry(
            form,
            width=250
        )

        self.item_entry.grid(
            row=3,
            column=1,
            padx=10,
            pady=10
        )

        # Notes

        ctk.CTkLabel(
            form,
            text="Notes"
        ).grid(
            row=4,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.note_entry = ctk.CTkEntry(
            form,
            width=250
        )

        self.note_entry.grid(
            row=4,
            column=1,
            padx=10,
            pady=10
        )

        # Save Button

        self.save_button = ctk.CTkButton(
            form,
            text="💾 Save Transaction",
            width=180
        )

        self.save_button.grid(
            row=5,
            column=1,
            pady=20
        )

        # ---------------------------------------
        # Transaction List
        # ---------------------------------------

        self.transaction_list = ctk.CTkScrollableFrame(
            self,
            width=800,
            height=300
        )

        self.transaction_list.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        ctk.CTkLabel(
            self.transaction_list,
            text="Today's Transactions (Coming Next Step)",
            font=("Arial", 18)
        ).pack(
            pady=20
        )