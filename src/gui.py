import customtkinter as ctk


# -----------------------------
# Application Settings
# -----------------------------
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class GroceryGUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("🛒 Grocery Voice Udhar Assistant")
        self.geometry("1200x700")
        self.minsize(1000, 600)

        self.create_sidebar()
        self.create_dashboard()

    # -----------------------------
    # Sidebar
    # -----------------------------
    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        title = ctk.CTkLabel(
            self.sidebar,
            text="🛒 Grocery Shop",
            font=("Arial", 22, "bold")
        )

        title.pack(pady=30)

        menu = [
            "🏠 Dashboard",
            "👤 Customers",
            "💰 Transactions",
            "📊 Reports",
            "⚙ Settings"
        ]

        for item in menu:

            btn = ctk.CTkButton(
                self.sidebar,
                text=item,
                height=40
            )

            btn.pack(
                padx=15,
                pady=8,
                fill="x"
            )

    # -----------------------------
    # Dashboard
    # -----------------------------
    def create_dashboard(self):

        self.content = ctk.CTkFrame(self)

        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        heading = ctk.CTkLabel(
            self.content,
            text="Dashboard",
            font=("Arial", 28, "bold")
        )

        heading.pack(pady=30)

        welcome = ctk.CTkLabel(
            self.content,
            text="Welcome to Grocery Voice Udhar Assistant",
            font=("Arial", 18)
        )

        welcome.pack(pady=10)


if __name__ == "__main__":

    app = GroceryGUI()
    app.mainloop()