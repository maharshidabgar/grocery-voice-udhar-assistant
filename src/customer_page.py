import customtkinter as ctk
from customer_manager import CustomerManager


class CustomerPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.manager = CustomerManager()

        self.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.create_widgets()

    def create_widgets(self):

        # Heading

        heading = ctk.CTkLabel(
            self,
            text="👤 Customer Management",
            font=("Arial", 28, "bold")
        )

        heading.pack(pady=(10, 20))

        # Form

        form = ctk.CTkFrame(self)

        form.pack(fill="x", padx=20)

        # Name

        ctk.CTkLabel(
            form,
            text="Customer Name"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.name_entry = ctk.CTkEntry(
            form,
            width=250
        )

        self.name_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        # Mobile

        ctk.CTkLabel(
            form,
            text="Mobile Number"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.mobile_entry = ctk.CTkEntry(
            form,
            width=250
        )

        self.mobile_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        # Add Button

        self.add_button = ctk.CTkButton(
            form,
            text="➕ Add Customer",
            width=180,
            command=self.add_customer
        )

        self.add_button.grid(
            row=2,
            column=1,
            pady=20
        )

        # Placeholder

        placeholder = ctk.CTkLabel(
            self,
            text="Customer Table (Coming Next Step)",
            font=("Arial", 18)
        )

        placeholder.pack(pady=40)

    # ---------------------------------------
    # Add Customer
    # ---------------------------------------

    def add_customer(self):

        name = self.name_entry.get().strip()
        mobile = self.mobile_entry.get().strip()

        try:

            message = self.manager.add_customer(
                name,
                mobile
            )

            print(message)

            self.name_entry.delete(0, "end")
            self.mobile_entry.delete(0, "end")

        except Exception as e:

            print(e)