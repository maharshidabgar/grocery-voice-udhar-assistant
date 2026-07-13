from voice_parser import VoiceParser

parser = VoiceParser()

while True:

    text = input("Speak Text : ")

    print(parser.parse(text))