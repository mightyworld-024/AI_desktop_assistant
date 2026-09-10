from core.memory import remember, recall


def process_query(query):

    query = query.lower().strip(" ?.!")

    # -------------------------------
    # SAVE NAME
    # -------------------------------

    if query.startswith("my name is "):

        name = query.replace("my name is ", "").strip()

        if name:
            remember("name", name)

            return f"Got it. I'll remember your name, {name}."


    # -------------------------------
    # RECALL NAME
    # -------------------------------

    if query in [
        "what is my name",
        "whats my name",
        "what's my name"
    ]:

        name = recall("name")

        if name:
            return f"Your name is {name}."

        return "I don't know your name yet."


    # -------------------------------
    # REMEMBER SOMETHING
    # -------------------------------

    if query.startswith("remember that "):

        information = query.replace(
            "remember that ",
            "",
            1
        ).strip()

        if information:
            remember("note", information)

            return "Got it. I'll remember that."


    # -------------------------------
    # CHECK MEMORY
    # -------------------------------

    if query in [
        "what do you remember",
        "what do you remember about me",
        "what do you know about me"
    ]:

        name = recall("name")
        note = recall("note")

        memories = []

        if name:
            memories.append(f"your name is {name}")

        if note:
            memories.append(note)

        if memories:
            return "I remember that " + " and ".join(memories) + "."

        return "I don't remember anything about you yet."


    # -------------------------------
    # NOTHING FOUND
    # -------------------------------

    return None