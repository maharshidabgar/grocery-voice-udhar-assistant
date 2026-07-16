import re
from difflib import get_close_matches

class VoiceParser:

    def __init__(self):

        # ------------------------------------
        # Grocery Dictionary
        # Spoken Name -> Standard Name
        # ------------------------------------

        self.item_map = {
            # ---------------- Milk ----------------
            "milk": "Milk",
            "doodh": "Milk",
            "doodhna": "Milk",
            "doodhno": "Milk",
            "doodh ni batli": "Milk",
            "dood": "Milk",
            "doodna": "Milk",
            "doodno": "Milk",
            "dud": "Milk",
            "dudno": "Milk",
            "dudna": "Milk",
            "dudhna": "Milk",
            "dudhno": "Milk",
            "nani doodh": "Milk",
            "nani doodhna": "Milk",
            "moti doodh": "Milk",
            "moti doodhna": "Milk",
            "goldna": "Milk",
            "gold milk": "Milk",
            "amul gold": "Milk",
            "amul goldna": "Milk",
            "taajana": "Milk",
            "taazana": "Milk",
            "taja": "Milk",
            "dhabudu": "Milk",
            # ---------------- Rice ----------------
            "rice": "Rice",
            "chokha": "Rice",
            "bhatnachokha": "Rice",
            "khichdinachokha": "Rice",
            "chokhana": "Rice",
            "basmati": "Rice",
            # ---------------- Flour ----------------
            "atta": "Atta",
            "lot": "Atta",
            "lotna": "Atta",
            "flour": "Atta",
            "ghau no lot": "Atta",
            "ghau no lotna": "Atta",
            "chana no lot": "Atta",
            "chana no lotna": "Atta",
            "besan": "Atta",
            # ---------------- Oil ----------------
            "oil": "Oil",
            "tel": "Oil",
            "telno": "Oil",
            "telna": "Oil",
            "fortune": "Oil",
            "sunflower": "Oil",
            # ---------------- Sugar ----------------
            "sugar": "Sugar",
            "khand": "Sugar",
            "khandna": "Sugar",
            # ---------------- Salt ----------------
            "salt": "Salt",
            "mithu": "Salt",
            "namak": "Salt",
            # ---------------- Tea ----------------
            "tea": "Tea",
            "cha": "Tea",
            "chana": "Tea",
            "cha": "Tea",
            "cha ni bhuki": "Tea",
            # ---------------- Dal ----------------
            "dal": "Dal",
            "dalna": "Dal",
            "tuver": "Dal",
            "tuvernidal": "Dal",
            "moong": "Dal",
            "magnidal": "Dal",
            "masoor": "Dal",
            # ---------------- Ghee ----------------
            "ghee": "Ghee",
            # ---------------- Butter ----------------
            "butter": "Butter",
            "makhan": "Butter",
            "DahiNikothli": "Butter",
            # ---------------- Soap ----------------
            "soap": "Soap",
            "sabun": "Soap",
            "sabuna": "Soap",
            # ---------------- Biscuit ----------------
            "biscuit": "Biscuit",
            "bikit": "Biscuit",
            # ---------------- Chocolate ----------------
            "chocolate": "Chocolate",
            "soklate": "Chocolate",
            # ---------------- Shampoo ----------------
            "shampoo": "Shampoo",
            # ---------------- Toothpaste ----------------
            "paste": "Toothpaste",
            "toothpaste": "Toothpaste",
            "toob": "Toothpaste",
            # ---------------- Eggs ----------------
            "egg": "Egg",
            "eggs": "Egg",
            "inda": "Egg",
            # ---------------- Bread ----------------
            "bread": "Bread",
            "pav": "Bread",
            "pavpatti": "Bread",
            "khari": "Bread",
            # ---------------- Maggi ----------------
            "maggi": "Maggi",
            "pasta": "Maggi",
            "noodles": "Maggi",
        }

        # ------------------------------------
        # Voice Correction Dictionary
        # ------------------------------------

        self.voice_alias = {

            # ---------------- Milk ----------------

            "dud": "doodh",
            "dude": "doodh",
            "dudena": "doodh",
            "dudeno": "doodh",
            "dudna": "doodh",
            "dudno": "doodh",
            "dudh": "doodh",
            "dudhna": "doodh",
            "dudhno": "doodh",
            "dood": "doodh",
            "doodna": "doodh",
            "doodno": "doodh",
            "doodhno": "doodh",
            "doodhna": "doodh",
            "doodh": "doodh",
            "dudi": "doodh",
            "dudu": "doodh",
            "milk": "doodh",

            # ---------------- Oil ----------------

            "tail": "tel",
            "telno": "tel",
            "telna": "tel",
            "oil": "tel",

            # ---------------- Rice ----------------

            "chokhano": "chokha",
            "chokhana": "chokha",
            "rice": "chokha",

            # ---------------- Flour ----------------

            "lotno": "lot",
            "lotna": "lot",
            "atta": "lot",
            "flour": "lot",

            # ---------------- Tea ----------------

            "chaano": "cha",
            "chano": "cha",
            "tea": "cha",

            # ---------------- Rupees ----------------

            "rs": "rupiya",
            "rupee": "rupiya",
            "rupees": "rupiya",
            "rupio": "rupiya",
            "rupiyo": "rupiya",
            "rupaiya": "rupiya",
            "paisa": "rupiya",

            # ---------------- Gujarati Numbers ----------------

            "ek": "1",
            "be": "2",
            "tran": "3",
            "char": "4",
            "panch": "5",
            "chh": "6",
            "sat": "7",
            "aath": "8",
            "nav": "9",
            "das": "10",

        }

        # ------------------------------------
        # Customer Alias Dictionary
        # ------------------------------------

        self.customer_alias = {

            # Ramesh
            "rames": "Ramesh",
            "rameh": "Ramesh",
            "ramehs": "Ramesh",
            "ramesh": "Ramesh",

            # Jenam
            "janam": "Jenam",
            "jenam": "Jenam",
            "jenem": "Jenam",
            "jena": "Jenam",
            "janem": "Jenam",

            # Ram Bhai
            "rambhai": "Ram Bhai",
            "rambhai": "Ram Bhai",
            "ram": "Ram Bhai",

            # Ikbal
            "ikbal": "Ikbal",
            "iqbal": "Ikbal",
            "ekbal": "Ikbal",

            # Hetal
            "hetal": "Hetal",

            # Atulgiri
            "atul": "Atulgiri",
            "atulgiri": "Atulgiri",
            "atulgiri": "Atulgiri",
        }

        # ------------------------------------
        # UDHAR Keywords
        # ------------------------------------

        self.udhar_keywords = [
            "udhar",
            "uda",  
            "udhaar",  
            "udhhar",  
            "baki",
            "baaki",
            "credit",
            "borrow",
            "khate",
            "khata",
            "lakh",
            "likh",
        ]

        # ------------------------------------
        # PAYMENT Keywords
        # ------------------------------------

        self.payment_keywords = [
            "payment",
            "pement",
            "pay",
            "paid",
            "jama",
            "jamma",
            "apya",
            "apay",
            "api",
            "aapya",
            "apyo",
            "api",
            "cash",
            "return",
        ]

        # ------------------------------------
        # Gujarati Quantity Words
        # ------------------------------------

        self.quantity_words = [
            "kilo",
            "kg",
            "gram",
            "gm",
            "liter",
            "ltr",
            "ml",
            "piece",
            "packet",
            "pack",
            "dozen",
        ]

        # ------------------------------------
        # Gujarati Number Words
        # ------------------------------------

        self.number_map = {

            "ek": 1,
            "be": 2,
            "tran": 3,
            "char": 4,
            "panch": 5,
            "chha": 6,
            "sat": 7,
            "aath": 8,
            "nav": 9,
            "das": 10,

            "so": 100,
            "basso": 200,
            "transo": 300,
            "charso": 400,
            "panchso": 500,
            "chhaso": 600,
            "satso": 700,
            "aathso": 800,
            "navso": 900,

            "hajar": 1000
        }

        # ------------------------------------
        # Add Customer Keywords
        # ------------------------------------

        self.add_customer_keywords = [

            "add customer",
            "customer add",
            "new customer",
            "create customer",
            "add",
            "create"

        ]

    # ------------------------------------
    # Detect Amount
    # ------------------------------------

    def find_amount(self, text):

        text = text.lower()

        # -----------------------------
        # First try numeric values
        # -----------------------------

        numbers = re.findall(r"\d+(?:\.\d+)?", text)

        if numbers:

            words = text.split()

            amount = None

            for i, word in enumerate(words):

                if re.fullmatch(r"\d+(?:\.\d+)?", word):

                    # Ignore quantity numbers
                    if i + 1 < len(words):

                        if words[i + 1] in self.quantity_words:

                            continue

                    amount = float(word)

            if amount is not None:

                return amount

        # -----------------------------
        # Gujarati Number Words
        # -----------------------------

        words = text.split()

        for word in words:

            if word in self.number_map:

                return float(self.number_map[word])

        return None

    # ------------------------------------
    # Detect Transaction Type
    # ------------------------------------

    def find_transaction_type(self, text):

        text = text.lower()
        
        for keyword in self.payment_keywords:

            if keyword in text:

                return "PAYMENT"

        for keyword in self.udhar_keywords:

            if keyword in text:

                return "UDHAR"

        return None

    # ------------------------------------
    # Detect Grocery Item
    # ------------------------------------

    def find_item(self, text):

        text = text.lower()

        # Exact Match
        items = sorted(
            self.item_map.keys(),
            key=len,
            reverse=True
        )

        for spoken_name in items:

            if spoken_name in text:

                return self.item_map[spoken_name]

        # Fuzzy Match
        words = text.split()

        for word in words:

            match = get_close_matches(
                word,
                self.item_map.keys(),
                n=1,
                cutoff=0.70
            )

            if match:

                return self.item_map[match[0]]

        return ""

    # ------------------------------------
    # Detect Customer
    # ------------------------------------

    def find_customer(self, text):

        words = text.lower().split()

        ignore_words = {
            "na",
            "no",
            "ni",
            "ne",
            "e",
            "rupiya",
            "rupiyo",
            "rupees",
            "rupee",
            "baki",
            "baaki",
            "udhar",
            "payment",
            "pay",
            "paid",
            "jama",
            "cash",
            "apya",
            "aapya",
            "apyo",
            "api",
            "kilo",
            "kg",
            "gram",
            "gm",
            "liter",
            "ltr",
            "ml",
            "piece",
            "packet",
            "pack",
            "dozen",
            "noo",
            "naa",
            "nii",
        }

        customer = []

        for word in words:

            if word in ignore_words:
                break

            if word in self.item_map:
                break

            if re.fullmatch(r"\d+(\.\d+)?", word):
                break

            customer.append(word.capitalize())

        name = " ".join(customer).lower().strip()

        if name in self.customer_alias:

            return self.customer_alias[name]

        match = get_close_matches(
            name,
            self.customer_alias.keys(),
            n=1,
            cutoff=0.65
        )

        if match:

            return self.customer_alias[match[0]]

        return " ".join(customer)

    # ------------------------------------
    # Clean Text
    # ------------------------------------

    def clean_text(self, text):

        text = text.replace("ek", "1")
        text = text.replace("be", "2")
        text = text.replace("tran", "3")
        text = text.replace("char", "4")
        text = text.replace("panch", "5")
        text = text.replace("chh", "6")
        text = text.replace("sat", "7")
        text = text.replace("aath", "8")
        text = text.replace("nav", "9")
        text = text.replace("das", "10")

        text = re.sub(r"\s+", " ", text)

        words = text.split()

        new_words = []

        for word in words:

            new_words.append(
                self.voice_alias.get(word, word)
            )

        text = " ".join(new_words)

        return text.strip()

    # ------------------------------------
    # Is Add Customer Command
    # ------------------------------------

    def is_add_customer(self, text):

        text = text.lower()

        for keyword in self.add_customer_keywords:

            if keyword in text:

                return True

        return False

    # ------------------------------------
    # Parse Voice Command
    # ------------------------------------

    def parse(self, text):

        if not text:

            return None

        text = self.clean_text(text)

        result = {
            "customer": "",
            "type": "",
            "amount": None,
            "item": "",
            "quantity": "",
            "original_text": text,
            "add_customer": False,
        }

        result["add_customer"] = self.is_add_customer(text)

        # -------------------------
        # Customer
        # -------------------------

        result["customer"] = self.find_customer(text)

        # -------------------------
        # Item
        # -------------------------

        result["item"] = self.find_item(text)

        # -------------------------
        # Amount
        # -------------------------

        result["amount"] = self.find_amount(text)

        # -------------------------
        # Transaction Type
        # -------------------------

        result["type"] = self.find_transaction_type(text)

        # -------------------------
        # Smart Gujarati Detection
        # -------------------------

        if not result["type"]:

            udhar_words = [
                "baki",
                "baaki",
                "udhar",
                "khate",
                "khata",
                "lakh",
                "likh",
            ]

            payment_words = [
                "payment",
                "pay",
                "paid",
                "jama",
                "cash",
                "apya",
                "aapya",
                "apyo",
                "api",
            ]

            if any(word in text for word in udhar_words):

                result["type"] = "UDHAR"

            elif any(word in text for word in payment_words):

                result["type"] = "PAYMENT"

        # -------------------------
        # Default Transaction
        # -------------------------

        if not result["type"]:

            result["type"] = "UDHAR"

        return result
