import customtkinter as ctk
from dashboard import Dashboard
from customer_page import CustomerPage
from transaction_page import TransactionPage

# Theme
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class GroceryGUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Window
        self.title("🛒 Grocery Voice Udhar Assistant")
        self.geometry("1200x700")
        self.minsize(1000, 600)

        # Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_content()

    # ----------------------------------------
    # Sidebar
    # ----------------------------------------

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        title = ctk.CTkLabel(
            self.sidebar,
            text="🛒 Grocery Shop",
            font=("Arial", 22, "bold")
        )

        title.pack(pady=(30, 20))

        buttons = [

            ("🏠 Dashboard", self.show_dashboard),

            ("👤 Customers", self.show_customers),

            ("💰 Transactions", self.show_transactions),

            ("📊 Reports", self.not_ready),

            ("⚙ Settings", self.not_ready)

        ]

        for text, command in buttons:

            button = ctk.CTkButton(
                self.sidebar,
                text=text,
                height=40,
                command=command
            )

            button.pack(
                fill="x",
                padx=15,
                pady=8
            )

    # ----------------------------------------
    # Content Area
    # ----------------------------------------

    def create_content(self):

        self.content = ctk.CTkFrame(self)

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=15,
            pady=15
        )

        self.show_dashboard()

    # ----------------------------------------
    # Clear Page
    # ----------------------------------------

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    # ----------------------------------------
    # Dashboard
    # ----------------------------------------

    def show_dashboard(self):

        self.clear_content()

        dashboard = Dashboard(self.content)

        dashboard.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    # ----------------------------------------
    # Customers
    # ----------------------------------------

    def show_customers(self):

        self.clear_content()

        page = CustomerPage(self.content)

        page.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    # ----------------------------------------
    # Transactions
    # ----------------------------------------

    def show_transactions(self):

        self.clear_content()

        page = TransactionPage(self.content)

        page.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    # ----------------------------------------
    # Placeholder Pages
    # ----------------------------------------

    def not_ready(self):

        self.clear_content()

        label = ctk.CTkLabel(
            self.content,
            text="🚧 This module is under development.",
            font=("Arial", 24, "bold")
        )

        label.pack(expand=True)


# ----------------------------------------
# Run Application
# ----------------------------------------

if __name__ == "__main__":

    app = GroceryGUI()
    app.mainloop()