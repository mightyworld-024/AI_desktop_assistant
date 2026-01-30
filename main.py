import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")

for i, voice in enumerate(voices):
    print(i, voice.name)
engine.setProperty("voice", voices[1].id)  # Set to female voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    return input("You: ").lower()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)                

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("You:", query)
        return query.lower()
    except:
        return "none"

def chatbot_reply(query):
    if "hello" in query or "hi" in query or "hlo" in query:
        return "Hello ,how are you?"
    
    elif "I am good " in query or "i am fine" in query or "m badhiya" in query:
        return "Ohh That's great to hear , How may I help you today?"
    
    elif "what is your purpose" in query or "how can you help me" in query:
        return "Mera purpose hai tumhari madad karna aur tumhare kaam ko aasan banana"

    elif "apne baare m batao" in query or "Tell me about yourself" in query:
        return "Main ek desktop voice assistant hoon jo tumhari madad karta hoon"
    
    elif "tell me about your features" in query or "What can you do" in query or "tell me about yourself" in query:
        return "I can act as your personal assistant, helping you with tasks like opening applications, searching the web, and answering your questions.compelete you task like searchng and opening your favourite websites and applications"
    
    elif "tum kaise ho" in query:
        return "Main theek hoon, tum kaise ho?"

    elif "how are you" in query:
        return "Main badiya hoon, tum bata?"

    elif "what's your name" in query:
        return "My Name is Venus . I am created by Sidharth Mitra"    
      

    elif "who made you" in query:
        return "Sidharth Mitra has created me in python version 3.8"

    else:
        return "Sorry I could not understand. Can you please rephrase?"

def handle_command(query):

    if "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        return True

    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://google.com")
        return True

    elif "open notepad" in query:
        speak("Opening Notepad")
        os.startfile("notepad.exe")
        return True
    
    elif query.startswith("search"):
        speak("Searching on Google")
        search_query = query.replace("search", "").strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        return True


    elif "open vscode" in query:
        speak("Opening Visual Studio Code")
        os.startfile(
            "C:\\Users\\Public\\Desktop\\Visual Studio Code"
        )
        return True

    return False

speak("Hello My name is Venus . I am your Desktop Voice Assistant. How can I help you?")

while True:
    query = take_command()

    if query == "none":
        continue

    if "exit" in query or "bye" in query:
        speak("Bye bhai, milte hain")
        break

    if handle_command(query):
        continue

    reply = chatbot_reply(query)
    speak(reply)
    print("Assistant:", reply)
