import re


class VoiceParser:

    def __init__(self):

        # -------------------------
        # Grocery Item Dictionary
        # -------------------------

        self.item_map = {

            # Milk
            "milk": "Milk",
            "doodh": "Milk",
            "nani doodh": "Milk",
            "taja": "Milk",
            "gold": "Milk",
            "dhabudu": "Milk",

            # Rice
            "rice": "Rice",
            "chokha": "Rice",
            "basmati": "Rice",

            # Wheat Flour
            "atta": "Atta",
            "lot": "Atta",
            "flour": "Atta",
            "chana no lot": "Atta",

            # Oil
            "oil": "Oil",
            "tel": "Oil",

            # Sugar
            "sugar": "Sugar",
            "khand": "Sugar",

            # Salt
            "salt": "Salt",
            "mithu": "Salt",
            "namak": "Salt",

            # Tea
            "tea": "Tea",
            "cha": "Tea",
            "cha ni bhuki": "Tea",

            # Dal
            "dal": "Dal",
            "lentils": "Dal",

            # Ghee
            "ghee": "Ghee",

            # Butter
            "butter": "Butter",
            "makhan": "Butter",

            # Soap
            "soap": "Soap",
            "sabun": "Soap",

            # Biscuit
            "biscuit": "Biscuit",

            # Chocolate
            "chocolate": "Chocolate",

            # Shampoo
            "shampoo": "Shampoo",

            # Toothpaste
            "toothpaste": "Toothpaste",
            "paste": "Toothpaste",

            # Eggs
            "egg": "Egg",
            "eggs": "Egg",

            # Bread
            "bread": "Bread",
            "pav": "Bread",
            # Maggi
            "maggi": "Maggi"
            
        }

        # -------------------------
        # Transaction Keywords
        # -------------------------

        self.udhar_keywords = [

            "udhar",
            "credit",
            "borrow",
            "baki",
            "baaki",
            "lakh",
            "likh",
            "dejo",
            "aapo",
            "api de",
            "khate",
            "khata"
        ]

        self.payment_keywords = [

            "payment",
            "paid",
            "pay",
            "apya",
            "api",
            "jama",
            "cash",
            "return",
            "bharpai",
            "aapya"
        ]

    # ---------------------------------------
    # Parse Voice Command
    # ---------------------------------------

    def parse(self, text):

        if not text:

            return None

        text = text.lower().strip()

        result = {

            "customer": None,
            "type": None,
            "amount": None,
            "item": ""
        }

        # ---------------------------------------
        # Amount
        # ---------------------------------------

        match = re.search(r"\d+(\.\d+)?", text)

        if match:

            result["amount"] = float(match.group())

        # ---------------------------------------
        # Transaction Type
        # ---------------------------------------

        if any(word in text for word in self.udhar_keywords):

            result["type"] = "UDHAR"

        elif any(word in text for word in self.payment_keywords):

            result["type"] = "PAYMENT"

        # ---------------------------------------
        # Customer Name
        # ---------------------------------------

        words = text.split()

        if len(words) > 0:

            result["customer"] = words[0].capitalize()

        # ---------------------------------------
        # Grocery Item
        # ---------------------------------------

        for word in words:

            if word in self.item_map:

                result["item"] = self.item_map[word]

                break

        return result


# ---------------------------------------
# Testing
# ---------------------------------------

if __name__ == "__main__":

    parser = VoiceParser()

    while True:

        text = input("\nSpeak : ")

        if text.lower() == "exit":

            break

        print(parser.parse(text))