import customtkinter as ctk
from dashboard import Dashboard

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
        self.create_dashboard()

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
            "🏠 Dashboard",
            "👤 Customers",
            "💰 Transactions",
            "📊 Reports",
            "⚙ Settings"
        ]

        for text in buttons:

            button = ctk.CTkButton(
                self.sidebar,
                text=text,
                height=40
            )

            button.pack(
                fill="x",
                padx=15,
                pady=8
            )

    # ----------------------------------------
    # Dashboard
    # ----------------------------------------

    def create_dashboard(self):

        self.content = ctk.CTkFrame(self)

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=15,
            pady=15
        )

        dashboard = Dashboard(self.content)

        dashboard.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )


# ----------------------------------------
# Run Application
# ----------------------------------------

if __name__ == "__main__":

    app = GroceryGUI()
    app.mainloop()