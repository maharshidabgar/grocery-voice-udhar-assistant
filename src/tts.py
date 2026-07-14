import pyttsx3

class TextToSpeech:

    def __init__(self):

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 165)

    def speak(self, message):

        print("Assistant :", message)

        self.engine.say(message)

        self.engine.runAndWait()

    # ---------------------------------------
    # English Item -> Gujarati
    # ---------------------------------------

    def gujarati_item(self, item):

        item_map = {

            "Milk": "દૂધ",
            "Rice": "ચોખા",
            "Oil": "તેલ",
            "Atta": "લોટ",
            "Sugar": "ખાંડ",
            "Salt": "મીઠું",
            "Tea": "ચા",
            "Dal": "દાળ",
            "Ghee": "ઘી",
            "Butter": "માખણ",
            "Soap": "સાબુ",
            "Biscuit": "બિસ્કીટ",
            "Chocolate": "ચોકલેટ",
            "Shampoo": "શેમ્પૂ",
            "Toothpaste": "ટૂથપેસ્ટ",
            "Egg": "ઇંડા",
            "Bread": "બ્રેડ",
            "Maggi": "મેગી"

        }

        return item_map.get(item, item)