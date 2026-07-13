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

        # Header

        header = ctk.CTkFrame(self.customer_list)

        header.pack(fill="x", padx=5, pady=5)

        ctk.CTkLabel(
            header,
            text="ID",
            width=60,
            font=("Arial", 15, "bold")
        ).grid(row=0, column=0)

        ctk.CTkLabel(
            header,
            text="Customer Name",
            width=250,
            font=("Arial", 15, "bold")
        ).grid(row=0, column=1)

        ctk.CTkLabel(
            header,
            text="Mobile",
            width=180,
            font=("Arial", 15, "bold")
        ).grid(row=0, column=2)

        # Data

        for customer in customers:

            row = ctk.CTkFrame(self.customer_list)

            row.pack(fill="x", padx=5, pady=3)

            ctk.CTkLabel(
                row,
                text=str(customer[0]),
                width=60
            ).grid(row=0, column=0)

            ctk.CTkLabel(
                row,
                text=customer[1],
                width=250,
                anchor="w"
            ).grid(row=0, column=1)

            ctk.CTkLabel(
                row,
                text=customer[2],
                width=180
            ).grid(row=0, column=2)