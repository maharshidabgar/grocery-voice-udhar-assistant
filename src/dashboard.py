import customtkinter as ctk
from dashboard_manager import DashboardManager


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.manager = DashboardManager()

        self.create_widgets()

    # ---------------------------------------
    # Dashboard UI
    # ---------------------------------------

    def create_widgets(self):

        # Heading

        heading = ctk.CTkLabel(
            self,
            text="📊 Dashboard",
            font=("Arial", 30, "bold")
        )

        heading.pack(pady=(15, 5))

        # Status

        status = ctk.CTkLabel(
            self,
            text="🟢 Database Connected",
            font=("Arial", 15)
        )

        status.pack()

        # Cards Container

        self.cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.cards_frame.pack(
            pady=35
        )

        self.cards_frame.grid_columnconfigure(0, weight=1)
        self.cards_frame.grid_columnconfigure(1, weight=1)

        self.cards_frame.grid_rowconfigure(0, weight=1)
        self.cards_frame.grid_rowconfigure(1, weight=1)

        # Dashboard Cards

        self.create_card(
            "👥 Total Customers",
            str(self.manager.total_customers()),
            0,
            0
            )

        self.create_card(
            "💰 Today's Udhar",
            f"₹{self.manager.today_udhar():.2f}",
            0,
            1
        )

        self.create_card(
            "💵 Today's Payment",
            f"₹{self.manager.today_payment():.2f}",
            1,
            0
        )

        self.create_card(
            "📦 Pending Balance",
            f"₹{self.manager.pending_balance():.2f}",
            1,
            1
        )
    
    # ---------------------------------------
    # Card Widget
    # ---------------------------------------

    def create_card(self, title, value, row, column):

        card = ctk.CTkFrame(
            self.cards_frame,
            width=270,
            height=150,
            corner_radius=18
        )

        card.grid(
            row=row,
            column=column,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        card.grid_propagate(False)

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 17, "bold")
        )

        title_label.pack(
            pady=(30, 10)
        )

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 30, "bold")
        )

        value_label.pack()