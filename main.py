import subprocess
import webbrowser
import os
import pyttsx3
import time
from threading import Lock
import datetime
from core.memory import initialize_memory
from core.assistant import process_query
from tools.calculator import natural_calculation
# ==========================================
# INITIALIZE MEMORY
# ==========================================
initialize_memory()
# ==========================================
# TEXT TO SPEECH
# ==========================================
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
# ==========================================
# CHROME
# ==========================================
def open_chrome(url):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if os.path.exists(chrome_path):
        subprocess.Popen([
            chrome_path,
            "--profile-directory=Profile 1",
            url
        ])
    else:
        webbrowser.open(url)

# ==========================================
# BASIC CHATBOT
# =========================================
def chatbot_reply(query):

    if any(word in query for word in [
        "hello",
        "hi",
        "hlo",
        "hey"
    ]):
        return "Hello 🙌, how are you?"

    elif any(word in query for word in [
        "i am good",
        "i am fine",
        "mai theek hoon",
        "badhiya"
    ]):
        return "Oh that's great 👌 to hear. How may I help you today?"

    elif any(word in query for word in [
        "what is the time",
        "time",
        "time please",
        "current time",
        "time batao"
    ]):
        return "Current time is " + time.strftime("%I:%M %p")

    elif any(word in query for word in [
        "what is the date",
        "date",
        "date please",
        "current date",
        "date batao"
    ]):
        return (
            "Current date is "
            + datetime.datetime.now().strftime("%d/%m/%Y")
        )

    elif any(word in query for word in [
        "what is your purpose",
        "how can you help me",
        "mere lie kya kar sakte ho"
    ]):
        return (
            "Mera purpose hai tumhari madad 🤝 "
            "karna aur tumhare kaam ko aasan banana."
        )

    elif any(word in query for word in [
        "apne baare m batao",
        "tell me about yourself",
        "who are you"
    ]):
        return (
            "Main Venus hoon 🦸, "
            "ek desktop voice assistant jo tumhari madad karta hoon."
        )

    elif any(word in query for word in [
        "tell me about your features",
        "what can you do"
    ]):
        return (
            "I can act as your personal assistant. "
            "I can open applications, search the web, "
            "and help you with your daily tasks."
        )

    elif any(word in query for word in [
        "tum kaise ho",
        "kaise ho tum"
    ]):
        return (
            "Main theek hoon sab badhiya chal reha hai, "
            "tum kaise ho?"
        )

    elif any(word in query for word in [
        "how are you",
        "how are you doing",
        "kya haal chaal"
    ]):
        return "Main badiya hoon, tum bata?"

    elif any(word in query for word in [
        "what's your name",
        "your name"
    ]):
        return (
            "My name is Venus. "
            "I am created by Sidharth Mitra."
        )

    elif any(word in query for word in [
        "who made you",
        "who created you"
    ]):
        return (
            "Mr. Sidharth Mitra programmed me "
            "using Python version 3.10."
        )
    else:
        return "Sorry, I could not understand. Can you please rephrase?"
# ==========================================
# COMMAND HANDLER
# ==========================================
def handle_command(query):
    # --------------------------------------
    # YOUTUBE
    # --------------------------------------
    if "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        return True
    # --------------------------------------
    # WHATSAPP
    # --------------------------------------
    elif "open whatsapp" in query:
        speak("Opening WhatsApp")
        os.system("start whatsapp:")
        return True
    # --------------------------------------
    # GOOGLE
    # --------------------------------------
    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://google.com")
        return True
    # --------------------------------------
    # NETFLIX
    # --------------------------------------
    elif "open netflix" in query:
        speak("Opening Netflix")
        open_chrome("https://netflix.com")
        return True
    # --------------------------------------
    # RESUME
    # --------------------------------------
    elif "open my resume" in query:
        speak("Opening your resume")
        webbrowser.open(
            "https://mightyworld-024.github.io/Sidharth_Mitra_CV/"
        )
        return True
    # --------------------------------------
    # GITHUB
    # --------------------------------------
    elif "open my github" in query:
        speak("Opening your GitHub profile")
        webbrowser.open(
            "https://github.com/mightyworld-024"
        )
        return True
    # --------------------------------------
    # CALCULATOR
    # --------------------------------------
    elif "open calculator" in query:
        speak("Opening Calculator")
        os.startfile("calc.exe")
        return True
    # --------------------------------------
    # NOTEPAD
    # -------------------------------------
    elif "open notepad" in query:
        speak("Opening Notepad")
        os.startfile("notepad.exe")
        return True
    # --------------------------------------
    # SHUTDOWN
    # --------------------------------------
    elif "shutdown system" in query:
        speak("Shutting down system")
        os.system("shutdown /s /t 5")
        return True
    # --------------------------------------
    # RESTART
    # --------------------------------------
    elif "restart system" in query:
        speak("Restarting system")
        os.system("shutdown /r /t 5")
        return True
    # --------------------------------------
    # SEARCH
    # -------------------------------------
    elif query.startswith("search"):
        speak("Searching")
        # Netflix search
        if "on netflix" in query:
            term = (
                query
                .replace("search", "", 1)
                .replace("on netflix", "")
                .strip()
                .replace(" ", "%20")
            )
            url = f"https://www.netflix.com/search?q={term}"

        # YouTube search
        elif "on youtube" in query:
            term = (
                query
                .replace("search", "", 1)
                .replace("on youtube", "")
                .strip()
                .replace(" ", "+")
            )
            url = (
                f"https://www.youtube.com/results"
                f"?search_query={term}"
            )
        # Google search
        else:
            term = (
                query
                .replace("search", "", 1)
                .strip()
                .replace(" ", "+")
            )
            url = f"https://www.google.com/search?q={term}"
        open_chrome(url)
        return True

    return False
# ==========================================
# START VENUS
# ==========================================
speak(
    "Hello, I am Venus. "
    "How can I help you?"
)
# ==========================================
# MAIN LOOP
# ==========================================
while True:
    query = input("You: ").lower().strip()
    # --------------------------------------
    # EXIT
    # --------------------------------------
    if query in [
        "exit",
        "quit",
        "bye"
    ]:
        speak(
            "Goodbye. Have a nice day."
        )
        break
    # --------------------------------------
    # EMPTY INPUT
    # --------------------------------------
    if not query:
        continue
    # --------------------------------------
    # MEMORY / ASSISTANT
    # --------------------------------------
    assistant_reply = process_query(query)
    if assistant_reply:
        print("Venus:", assistant_reply)
        speak(assistant_reply)
        continue
    # --------------------------------------
    # COMMANDS
    # --------------------------------------
    if handle_command(query):
        continue

    # --------------------------------------
    # NATURAL LANGUAGE CALCULATOR
    # --------------------------------------
    calculation = natural_calculation(query)
    if calculation is not None:
        if isinstance(calculation, float) and calculation.is_integer():
            calculation = int(calculation)
        reply = f"The answer is {calculation}."
        print("Venus:", reply)
        speak(reply)
        continue
    # --------------------------------------
    # NORMAL CHATBOT
    # --------------------------------------
    reply = chatbot_reply(query)

    print("Venus:", reply)
    speak(reply)