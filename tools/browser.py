import subprocess
import webbrowser


CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def open_chrome(url):

    if not url:
        url = "https://www.google.com"

    if subprocess.os.path.exists(CHROME_PATH):

        subprocess.Popen([
            CHROME_PATH,
            "--profile-directory=Profile 1",
            url
        ])

    else:

        webbrowser.open(url)


def open_google():

    open_chrome("https://www.google.com")


def open_youtube():

    open_chrome("https://www.youtube.com")


def open_netflix():

    open_chrome("https://www.netflix.com")


def search_google(query):

    query = query.strip()

    url = "https://www.google.com/search?q=" + query.replace(" ", "+")

    open_chrome(url)


def search_youtube(query):

    query = query.strip()

    url = (
        "https://www.youtube.com/results?search_query="
        + query.replace(" ", "+")
    )

    open_chrome(url)


def search_netflix(query):

    query = query.strip()

    url = (
        "https://www.netflix.com/search?q="
        + query.replace(" ", "%20")
    )

    open_chrome(url)