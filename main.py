import speech_recognition as sr
import webbrowser
import os
import pyttsx3
import time
from threading import Lock
import datetime

speak_lock = Lock()

def speak(text):
    with speak_lock:
        print("Assistant:", text)
        engine.stop()
        engine.say(text)
        engine.runAndWait()
        time.sleep(0.2)   # 🔥 THIS LINE FIXES IT
        
engine = pyttsx3.init()
engine.setProperty("rate", 150)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # male (safe)

def speak(text):
    print("Assistant:", text)
    engine.stop()
    engine.say(text)
    engine.runAndWait()

def take_command():
    return input("You: ").lower()

def chatbot_reply(query):

    if any(word in query for word in ["hello", "hi", "hlo"]):
        return "Hello, how are you?"

    elif any(word in query for word in ["i am good", "i am fine", "mai theek hoon", "badhiya"]):
        return "Oh that's great to hear. How may I help you today?"
    
    elif any(word in query for word in ["what is the time","time", "time please", "current time", "time batao"]):
        return "current time is " + time.strftime("%I:%M %p")

    elif any(word in query for word in ["what is the date", "date","date please", "current date", "date batao"]):
        return "current date is " + datetime.datetime.now().strftime("%d/%m/%Y")

    elif any(word in query for word in ["what is your purpose", "how can you help me","mere lie kya kar sakte ho"]):
        return "Mera purpose hai tumhari madad karna aur tumhare kaam ko aasan banana."

    elif any(word in query for word in ["apne baare m batao", "tell me about yourself"]):
        return "Main Venus hoon, ek desktop voice assistant jo tumhari madad karta hoon."

    elif any(word in query for word in ["tell me about your features", "what can you do"]):
        return (
            "I can act as your personal assistant. "
            "I can open applications, search the web, "
            "and help you with your daily tasks."
        )
    
    elif any(word in query for word in ["tum kaise ho", "kaise ho tum"]):
        return "Main theek hoon sab badhiya chal reha hai, tum kaise ho?"

    elif any(word in query for word in ["how are you", "how are you doing","kya haal chaal"]):
        return "Main badiya hoon, tum bata?"

    elif any(word in query for word in ["what's your name", "your name"]):
        return "My name is Venus. I am created by Sidharth Mitra."

    elif any(word in query for word in ["who made you", "who created you"]):
        return "Mr.Sidharth Mitra has programed me using Python version 3.10."

    else:
        return "Sorry, I could not understand. Can you please rephrase?"

def handle_command(query):

    if "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        return True

    elif "open my resume" in query:
        speak("Opening your resume")
        webbrowser.open("https://mightyworld-024.github.io/Sidharth_Mitra_CV/")
        return True
    
    elif any(word in query for word in ["open google", "google open"]):
        speak("Opening Google")
        webbrowser.open("https://google.com")
        return True

    elif "open sheriyans" in query:
        speak("Opening Sheriyans")
        webbrowser.open("https://sheriyanscodeingschool.com")
        return True

    elif "open notepad" in query:
        speak("Opening Notepad")
        os.startfile("notepad.exe")
        return True

    elif query.startswith("search"):
        search_query = query.replace("search", "").strip()
        if search_query:
            speak(f"Searching for {search_query}")
            webbrowser.open(
                f"https://www.google.com/search?q={search_query}"
            )
        else:
            speak("What should I search for?")
        return True

    elif "open vscode" in query:
        speak("Opening Visual Studio Code")
        os.startfile(
            "C:\\Users\\Public\\Desktop\\Visual Studio Code"
        )
        return True

    return False

speak("Hello, my name is Venus. I am your desktop voice assistant. How can I help you?")

while True:
    query = take_command()

    if "exit" in query or "bye" in query or "quit" in query:
        speak("Goodbye. Have a nice day.")
        break

    if handle_command(query):
        continue

    reply = chatbot_reply(query)
    speak(reply)
