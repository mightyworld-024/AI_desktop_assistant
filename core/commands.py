import webbrowser

from tools.apps import (
    open_calculator,
    open_notepad,
    open_whatsapp,
)

from tools.browser import (
    open_google,
    open_youtube,
    open_netflix,
    search_google,
    search_youtube,
    search_netflix,
)

from tools.system import (
    shutdown_system,
    restart_system,
    cancel_shutdown,
)


def handle_command(query):

    query = query.lower().strip()


    # -------------------------------
    # OPEN YOUTUBE
    # -------------------------------

    if "open youtube" in query:

        open_youtube()

        return "Opening YouTube."


    # -------------------------------
    # OPEN WHATSAPP
    # -------------------------------

    if "open whatsapp" in query:

        open_whatsapp()

        return "Opening WhatsApp."


    # -------------------------------
    # OPEN GOOGLE
    # -------------------------------

    if "open google" in query:

        open_google()

        return "Opening Google."


    # -------------------------------
    # OPEN NETFLIX
    # -------------------------------

    if "open netflix" in query:

        open_netflix()

        return "Opening Netflix."


    # -------------------------------
    # OPEN RESUME
    # -------------------------------

    if "open my resume" in query:

        webbrowser.open(
            "https://mightyworld-024.github.io/Sidharth_Mitra_CV/"
        )

        return "Opening your resume."


    # -------------------------------
    # OPEN GITHUB
    # -------------------------------

    if "open my github" in query:

        webbrowser.open(
            "https://github.com/mightyworld-024"
        )

        return "Opening your GitHub profile."


    # -------------------------------
    # CALCULATOR
    # -------------------------------

    if "open calculator" in query:

        return open_calculator()


    # -------------------------------
    # NOTEPAD
    # -------------------------------

    if "open notepad" in query:

        return open_notepad()


    # -------------------------------
    # SHUTDOWN
    # -------------------------------

    if "shutdown system" in query:

        return shutdown_system()


    # -------------------------------
    # RESTART
    # -------------------------------

    if "restart system" in query:

        return restart_system()


    # -------------------------------
    # CANCEL SHUTDOWN
    # -------------------------------

    if "cancel shutdown" in query:

        return cancel_shutdown()


    # -------------------------------
    # SEARCH NETFLIX
    # -------------------------------

    if query.startswith("search") and "on netflix" in query:

        term = query.replace("search", "", 1)

        term = term.replace("on netflix", "")

        term = term.strip()

        search_netflix(term)

        return f"Searching Netflix for {term}."


    # -------------------------------
    # SEARCH YOUTUBE
    # -------------------------------

    if query.startswith("search") and "on youtube" in query:

        term = query.replace("search", "", 1)

        term = term.replace("on youtube", "")

        term = term.strip()

        search_youtube(term)

        return f"Searching YouTube for {term}."


    # -------------------------------
    # GOOGLE SEARCH
    # -------------------------------

    if query.startswith("search"):

        term = query.replace("search", "", 1).strip()

        if term:

            search_google(term)

            return f"Searching Google for {term}."


    return None