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

    # ---------------------------------------
    # Create Widgets
    # ---------------------------------------

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

        # Customer Name

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

        # Mobile Number

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

        # Add Customer Button

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

        # ---------------------------------------
        # Customer List
        # ---------------------------------------

        self.customer_list = ctk.CTkScrollableFrame(
            self,
            width=700,
            height=300
        )

        self.customer_list.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.load_customers()

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

            self.load_customers()

        except Exception as e:

            print(e)

    # ---------------------------------------
    # Load Customers
    # ---------------------------------------

    def load_customers(self):

        for widget in self.customer_list.winfo_children():
            widget.destroy()

        customers = self.manager.get_all_customers()

        if not customers:

            ctk.CTkLabel(
                self.customer_list,
                text="No customers found.",
                font=("Arial", 16)
            ).pack(pady=20)

            return

        header = ctk.CTkLabel(
            self.customer_list,
            text=f"{'ID':<5}{'Name':<25}{'Mobile'}",
            font=("Courier New", 16, "bold")
        )

        header.pack(
            anchor="w",
            padx=10,
            pady=(10, 5)
        )

        for customer in customers:

            row = ctk.CTkLabel(
                self.customer_list,
                text=f"{customer[0]:<5}{customer[1]:<25}{customer[2]}",
                font=("Courier New", 15)
            )

            row.pack(
                anchor="w",
                padx=10,
                pady=2
            )