import os
import tempfile
import whisper
import sounddevice as sd
import soundfile as sf


class VoiceAssistant:

    def __init__(self):

        print("Loading Whisper Model...")

        # tiny = Fast
        # base = Better Accuracy
        self.model = whisper.load_model("base")

        print("Whisper Ready ✅")

    def listen(self):

        temp_file = None

        try:

            sample_rate = 16000
            duration = 8

            print("🎤 Speak now...")

            audio = sd.rec(
                int(sample_rate * duration),
                samplerate=sample_rate,
                channels=1,
                dtype="float32"
            )

            sd.wait()

            with tempfile.NamedTemporaryFile(
                suffix=".wav",
                delete=False
            ) as f:

                temp_file = f.name

            sf.write(
                temp_file,
                audio,
                sample_rate
            )

            result = self.model.transcribe(
                temp_file,
                fp16=False,
                task="transcribe"
            )

            text = result["text"].strip()

            print("Detected Language :", result.get("language"))

            print("Original Text :", text)
            
            return text.lower()

        except Exception as e:

            print("Voice Error :", e)

            return None

        finally:

            if temp_file and os.path.exists(temp_file):

                try:
                    os.remove(temp_file)
                except:
                    pass