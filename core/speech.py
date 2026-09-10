import pyttsx3
from threading import Lock


speak_lock = Lock()

engine = pyttsx3.init()

engine.setProperty("rate", 150)

voices = engine.getProperty("voices")

try:
    engine.setProperty("voice", voices[1].id)
except:
    engine.setProperty("voice", voices[0].id)


def speak(text):

    with speak_lock:

        engine.stop()

        engine.say(text)

        engine.runAndWait()