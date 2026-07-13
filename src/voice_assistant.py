import speech_recognition as sr


class VoiceAssistant:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):

        try:

            with sr.Microphone() as source:

                print("🎤 Listening...")

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=1
                )

                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=8
                )

            text = self.recognizer.recognize_google(
                audio
            )

            print("You said:", text)

            return text.lower()

        except sr.WaitTimeoutError:
            return None

        except sr.UnknownValueError:
            return None

        except sr.RequestError:
            return None

        except Exception as e:
            print(e)
            return None