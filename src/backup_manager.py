import shutil
from tkinter import filedialog
from tkinter import messagebox


class BackupManager:

    def __init__(self):

        self.database = "database/shop_udhar.db"

    # ---------------------------------------
    # Backup
    # ---------------------------------------

    def backup_database(self):

        file = filedialog.asksaveasfilename(
            defaultextension=".db",
            filetypes=[
                ("Database File", "*.db")
            ],
            initialfile="Shop_Udhar_Backup.db"
        )

        if not file:
            return

        shutil.copy2(
            self.database,
            file
        )

        messagebox.showinfo(
            "Backup",
            "✅ Backup Created Successfully."
        )

    # ---------------------------------------
    # Restore
    # ---------------------------------------

    def restore_database(self):

        file = filedialog.askopenfilename(
            filetypes=[
                ("Database File", "*.db")
            ]
        )

        if not file:
            return

        shutil.copy2(
            file,
            self.database
        )

        messagebox.showinfo(
            "Restore",
            "✅ Database Restored Successfully.\n\nPlease restart the application."
        )