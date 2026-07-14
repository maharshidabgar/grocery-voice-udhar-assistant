import speech_recognition as sr


class VoiceAssistant:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8

    def listen(self):

        try:

            with sr.Microphone() as source:

                print("🎤 Listening...")

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=2
                )

                audio = self.recognizer.listen(
                    source,
                    timeout=8,
                    phrase_time_limit=10
                )

            text = self.recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print("You said :", text)

            return text.lower()

        except sr.WaitTimeoutError:

            print("No speech detected.")

            return None

        except sr.UnknownValueError:

            print("Could not understand voice.")

            return None

        except sr.RequestError as e:

            print("Speech Recognition Error :", e)

            return None

        except Exception as e:

            print("Voice Error :", e)

            return None