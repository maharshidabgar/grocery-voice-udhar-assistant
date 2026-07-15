import customtkinter as ctk
from difflib import get_close_matches

from customer_manager import CustomerManager
from transaction_manager import TransactionManager

from voice_assistant import VoiceAssistant
from voice_parser import VoiceParser

from tts import TextToSpeech

class TransactionPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.customer_manager = CustomerManager()
        self.transaction_manager = TransactionManager()

        self.voice = VoiceAssistant()
        self.parser = VoiceParser()
        self.tts = TextToSpeech()
    

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

        heading.pack(
            pady=(10, 20)
        )

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
            values=[]
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
            width=180,
            command=self.save_transaction
        )

        self.save_button.grid(
            row=5,
            column=1,
            pady=20
        )

        self.voice_button = ctk.CTkButton(
            form,
            text="🎤 Voice Input",
            width=180,
            command=self.voice_transaction
        )

        self.voice_button.grid(
            row=6,
            column=1,
            pady=10
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

        self.load_today_transactions()

        self.load_customers()

    # ---------------------------------------
    # Load Customers
    # ---------------------------------------

    def load_customers(self):

        customers = self.customer_manager.get_all_customers()

        if not customers:

            self.customer_option.configure(
                values=["No Customers"]
            )

            self.customer_option.set(
                "No Customers"
            )

            return

        customer_names = []

        for customer in customers:

            customer_names.append(
                customer[1]
            )

        self.customer_option.configure(
            values=customer_names
        )

        self.customer_option.set(
            customer_names[0]
        )

    # ---------------------------------------
    # Get Selected Customer ID
    # ---------------------------------------

    def get_selected_customer_id(self):

        selected_name = self.customer_option.get()

        customer = self.customer_manager.find_customer_by_name(
            selected_name
        )

        if customer:

            return customer[0]

        return None

    # ---------------------------------------
    # Save Transaction
    # ---------------------------------------

    def save_transaction(self):

        try:

            customer_id = self.get_selected_customer_id()

            if customer_id is None:

                print("Customer not selected.")
                return

            amount_text = self.amount_entry.get().strip()

            if amount_text == "":

                print("Amount is required.")
                return

            amount = float(amount_text)

            item_name = self.item_entry.get().strip()

            note = self.note_entry.get().strip()

            transaction_type = self.transaction_type.get()

            # -------------------------
            # Save Transaction
            # -------------------------

            if transaction_type == "UDHAR":

                message = self.transaction_manager.add_udhar(
                    customer_id,
                    amount,
                    item_name,
                    note
                )

            else:

                message = self.transaction_manager.add_payment(
                    customer_id,
                    amount,
                    note
                )

            print(message)

            # -------------------------
            # Gujarati Voice Response
            # -------------------------

            customer_name = self.customer_option.get()

            item_name = self.tts.gujarati_item(item_name)

            if transaction_type == "UDHAR":

                if amount == 1:

                    speech = (
                        f"{customer_name} ભાઈ, "
                        f"{item_name} નો 1 રૂપિયો "
                        f"બાકી લખાઈ ગયો."
                    )

                elif amount == 2:

                    speech = (
                        f"{customer_name} ભાઈ, "
                        f"{item_name} ના 2 રૂપિયા "
                        f"બાકી લખાઈ ગયા."
                    )

                else:

                    speech = (
                        f"{customer_name} ભાઈ, "
                        f"{item_name} ના {int(amount)} રૂપિયા "
                        f"બાકી લખાઈ ગયા."
                    )

            else:

                if amount == 1:

                    speech = (
                        f"{customer_name} ભાઈ, "
                        f"1 રૂપિયો જમા થયો."
                    )

                elif amount == 2:

                    speech = (
                        f"{customer_name} ભાઈ, "
                        f"2 રૂપિયા જમા થયા."
                    )

                else:

                    speech = (
                        f"{customer_name} ભાઈ, "
                        f"{int(amount)} રૂપિયા જમા થયા."
                    )

            print(speech)

            self.tts.speak(speech)

            # -------------------------
            # Clear Form
            # -------------------------

            self.amount_entry.delete(0, "end")
            self.item_entry.delete(0, "end")
            self.note_entry.delete(0, "end")

            self.transaction_type.set("UDHAR")

            # -------------------------
            # Refresh
            # -------------------------

            self.load_today_transactions()

        except Exception as e:

            print("Save Transaction Error :", e)


    # ---------------------------------------
    # Voice Customer
    # ---------------------------------------

    def voice_customer(self):

        self.tts.speak("ગ્રાહકનું નામ બોલો.")

        text = self.voice.listen()

        if not text:

            return None

        print("Customer :", text)

        return text

    # ---------------------------------------
    # Voice Item
    # ---------------------------------------

    def voice_item(self):

        self.tts.speak("વસ્તુ બોલો.")

        text = self.voice.listen()

        if not text:

            return None

        print("Item :", text)

        return text

    # ---------------------------------------
    # Voice Amount
    # ---------------------------------------

    def voice_amount(self):

        self.tts.speak("રકમ બોલો.")

        text = self.voice.listen()

        if not text:

            return None

        print("Amount :", text)

        return text

    # ---------------------------------------
    # Voice Type
    # ---------------------------------------

    def voice_type(self):

        self.tts.speak("ઉધાર કે પેમેન્ટ બોલો.")

        text = self.voice.listen()

        if not text:

            return None

        print("Type :", text)

        return text

    # ---------------------------------------
    # Voice Transaction Wizard
    # ---------------------------------------

    def voice_transaction(self):

        try:

            # -----------------------------
            # Customer
            # -----------------------------

            customer = self.voice_customer()

            if not customer:

                self.tts.speak("ગ્રાહક મળ્યો નથી.")

                return

            data = self.parser.parse(customer)

            print(data)

            if data["customer"]:

                customers = self.customer_manager.get_all_customers()

                customer_names = [
                    c[1]
                    for c in customers
                ]

                match = get_close_matches(
                    data["customer"],
                    customer_names,
                    n=1,
                    cutoff=0.50
                )

                if match:

                    self.customer_option.set(
                        match[0]
                    )

                else:

                    self.tts.speak(
                        "ગ્રાહક મળ્યો નથી."
                    )

                    return

            # -----------------------------
            # Item
            # -----------------------------

            item = self.voice_item()

            if item:

                data = self.parser.parse(item)

                self.item_entry.delete(0, "end")

                if data["item"]:

                    self.item_entry.insert(
                        0,
                        data["item"]
                    )

            # -----------------------------
            # Amount
            # -----------------------------

            amount = self.voice_amount()

            if amount:

                data = self.parser.parse(amount)

                self.amount_entry.delete(
                    0,
                    "end"
                )

                if data["amount"]:

                    self.amount_entry.insert(
                        0,
                        str(int(data["amount"]))
                    )

            # -----------------------------
            # Transaction Type
            # -----------------------------

            transaction = self.voice_type()

            if transaction:

                data = self.parser.parse(
                    transaction
                )

                if data["type"]:

                    self.transaction_type.set(
                        data["type"]
                    )

            # -----------------------------
            # Save
            # -----------------------------

            self.save_transaction()

        except Exception as e:

            print(
                "Voice Wizard Error :",
                e
            )
    
    # ---------------------------------------
    # Today's Transactions
    # ---------------------------------------

    def load_today_transactions(self):

        for widget in self.transaction_list.winfo_children():

            widget.destroy()

        transactions = self.transaction_manager.get_today_transactions()

        if not transactions:

            ctk.CTkLabel(
                self.transaction_list,
                text="No transactions today.",
                font=("Arial", 16)
            ).pack(
                pady=20
            )

            return

        # Header

        header = ctk.CTkFrame(
            self.transaction_list
        )

        header.pack(
            fill="x",
            padx=5,
            pady=5
        )

        headings = [
            "Customer",
            "Type",
            "Amount",
            "Item",
            "Note",
            "Time"
        ]

        for col, title in enumerate(headings):

            ctk.CTkLabel(
                header,
                text=title,
                width=120,
                font=("Arial", 14, "bold")
            ).grid(
                row=0,
                column=col,
                padx=5
            )

        # Data

        for transaction in transactions:

            row = ctk.CTkFrame(
                self.transaction_list
            )

            row.pack(
                fill="x",
                padx=5,
                pady=2
            )

            for col, value in enumerate(transaction):

                ctk.CTkLabel(
                    row,
                    text=str(value),
                    width=120,
                    anchor="w"
                ).grid(
                    row=0,
                    column=col,
                    padx=5
                )