import os
import subprocess


def open_calculator():

    os.startfile("calc.exe")

    return "Opening Calculator."


def open_notepad():

    os.startfile("notepad.exe")

    return "Opening Notepad."


def open_whatsapp():

    os.system("start whatsapp:")

    return "Opening WhatsApp."


def open_chrome():

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    if os.path.exists(chrome_path):

        subprocess.Popen([
            chrome_path
        ])

        return "Opening Chrome."

    return "Chrome was not found on this computer."