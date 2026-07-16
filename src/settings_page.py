import customtkinter as ctk

from src.backup_manager import BackupManager


class SettingsPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.backup_manager = BackupManager()

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
            text="⚙️ Settings",
            font=("Arial", 30, "bold")
        )

        heading.pack(
            pady=(20, 40)
        )

        button_frame = ctk.CTkFrame(self)

        button_frame.pack(
            pady=20
        )

        ctk.CTkButton(
            button_frame,
            text="💾 Backup Database",
            width=260,
            height=45,
            command=self.backup_manager.backup_database
        ).pack(
            pady=10
        )

        ctk.CTkButton(
            button_frame,
            text="♻️ Restore Database",
            width=260,
            height=45,
            command=self.backup_manager.restore_database
        ).pack(
            pady=10
        )