import pyttsx3


class TextToSpeech:

    def __init__(self):

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 165)

    def speak(self, message):

        print("Assistant :", message)

        self.engine.say(message)

        self.engine.runAndWait()